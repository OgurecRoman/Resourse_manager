from .models import Machine
from .serializers import MachineSerializer
from rest_framework import viewsets


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all().order_by('name')
    serializer_class = MachineSerializer
