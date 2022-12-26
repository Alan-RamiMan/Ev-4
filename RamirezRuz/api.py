from .models import CarrerasModel
from rest_framework import viewsets,permissions
from .serializers import CarrerasSerializer


class CarrerasViewSet(viewsets.ModelViewSet):
    queryset=CarrerasModel.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CarrerasSerializer