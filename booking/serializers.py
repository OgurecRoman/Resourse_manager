from rest_framework import serializers
from .models import Machine, Booking


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = (
            'name',
            'password',
            'status',
            'cpuCores',
            'ram',
            'ssd',
            'ipv4',
            'ipv6',
            'bandwidth',
            'operatingSystem',
            'status',
        )


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'machine',
            'bookedBy',
            'bookedFrom',
            'bookedUntil',
        )
