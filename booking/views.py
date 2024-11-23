from django.db.models import Q
import datetime
from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions

from .models import Machine, Booking
from .serializers import (
    MachineSerializer,
    GroupSerializer,
    UserSerializer,
    BookingSerializer,
)
from .permissions import IsOwner, IsSuperUser


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get_queryset(self):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start and end:
            startDate = datetime.datetime.strptime(start, "%Y-%m-%d-%H:%M")
            endDate = datetime.datetime.strptime(end, "%Y-%m-%d-%H:%M")

            busy_machines = Booking.objects.filter(
                Q(bookedFrom__lt=endDate) & Q(bookedUntil__gt=startDate)
            )

            machines = busy_machines.values_list('machine_id', flat=True)

            queryset = Machine.objects.exclude(id__in=machines)
            return queryset
        return []


def book(request, pk):
    start = request.query_params.get("start")
    end = request.query_params.get("end")
    if start and end:
        machine = Machine.objects.get(id=pk)
        machine.status = "booking"
        machine.save()

        newBook = Booking(machine=machine,
                          ownedBy=request.user,
                          start=start,
                          end=end)
        newBook.save()


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
