from platform import machine

from .models import Machine, Booking
from .serializers import MachineSerializer, BookingSerializer
from rest_framework import viewsets
from django.db.models import Q
import datetime


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


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


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
