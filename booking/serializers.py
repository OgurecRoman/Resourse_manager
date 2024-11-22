from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Machine, Booking
from .permissions import IsOwner, IsSuperUser


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
        fields = ['id', 'machine', 'bookedUntil', 'bookedFrom']

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [
                IsSuperUser,
            ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
