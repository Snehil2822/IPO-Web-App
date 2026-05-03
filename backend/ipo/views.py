from rest_framework.generics import ListAPIView
from .models import IPO
from .serializers import IPOSerializer


class IPOListView(ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer