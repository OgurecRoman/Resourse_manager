from rest_framework import serializers
from .models import Machine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('name', 'password', 'spuCores', 'ram', 'ssd',
                  'ip', 'bandwidth', 'operating_system')
