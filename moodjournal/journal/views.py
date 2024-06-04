from rest_framework import permissions, viewsets
from .models import Journal
from .serializers import JournalSerializer

# Create your views here.


class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Journal.objects.all().order_by('-created_at')
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
