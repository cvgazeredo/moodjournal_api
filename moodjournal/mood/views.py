from rest_framework import viewsets, permissions
from .models import Mood
from .serializers import MoodSerializer

# Create your views here.


class MoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Mood.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MoodSerializer
