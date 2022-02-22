from rest_framework import viewsets
from .serializers import WaitlistSerializer
from .models import Waitlist


class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer
