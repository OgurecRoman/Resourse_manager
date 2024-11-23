from django.db.models import Q
import datetime
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Machine, Booking
from .serializers import (
    MachineSerializer,
    BookingSerializer,
)
from .permissions import IsOwner, IsSuperUser


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticated]

    # мы игнорируем то состояние, когда человек без проверки на то, что
    # машина свободна её бронирует.
    @action(detail=True, methods=['get', 'post'])
    def book(self, request, pk):
        start = request.query_params.get('start', '')
        end = request.query_params.get('end', '')
        try:
            start_datetime = datetime.datetime.strptime(
                start, '%Y-%m-%d-%H:%M'
            )
            end_datetime = datetime.datetime.strptime(end, '%Y-%m-%d-%H:%M')
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if start_datetime and end_datetime:
            if end_datetime < start_datetime:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            try:
                machine = Machine.objects.get(id=pk)
            except Machine.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)
            machine.status = Machine.StatusEnum.BOOKED
            machine.save()

            new_booking = Booking.objects.create(
                machine=machine,
                bookedBy=request.user,
                bookedFrom=start_datetime,
                bookedUntil=end_datetime,
            )
            new_booking.save()
            serializer = BookingSerializer(new_booking, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return {}

    @action(detail=False, methods=['GET'])
    def available(self, request):
        """Gets all machines that are not booked in specified time interval."""
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        if start and end:
            start_date = datetime.datetime.strptime(start, '%Y-%m-%d-%H:%M')
            end_date = datetime.datetime.strptime(end, '%Y-%m-%d-%H:%M')

            busy_machines = Booking.objects.filter(
                Q(bookedFrom__lt=end_date) & Q(bookedUntil__gt=start_date)
            )

            machines = busy_machines.values_list('machine_id', flat=True)

            active_non_booked_machines = Machine.objects.exclude(
                id__in=machines
            ).filter(status=Machine.StatusEnum.ACTIVE)
            serializer = self.get_serializer(
                active_non_booked_machines, many=True
            )
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def my(self, request):
        now = datetime.datetime.now()
        user_current_bookings = Booking.objects.filter(
            Q(bookedBy=request.user) & Q(bookedUntil__gt=now)
        )
        user_machines = user_current_bookings.values_list('machine_id', flat=True)
        user_machines = Machine.objects.filter(Q(pk__in=user_machines))
        serializer = self.get_serializer(user_machines, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        machine = Machine.objects.get(pk=self.request.data['machine'][0])
        serializer.save(bookedBy=self.request.user, machine=machine)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [
                IsSuperUser,
            ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()

    @action(detail=False, methods=['get'])
    def history(self, request):
        queryset = Booking.objects.filter(bookedBy=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
