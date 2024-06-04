from rest_framework import permissions, viewsets
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Patient.objects.all().order_by('-date_joined')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
