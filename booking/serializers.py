from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Machine, Booking


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = (
            'pk',
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
        fields = ["id", "machine", "bookedUntil", "bookedFrom"]



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
