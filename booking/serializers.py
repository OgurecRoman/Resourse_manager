from rest_framework import serializers
from .models import Machine


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
