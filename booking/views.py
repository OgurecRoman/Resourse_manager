from .models import Machine
from .serializers import MachineSerializer
from rest_framework import viewsets


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get_queryset(self):
        queryset = Machine.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
