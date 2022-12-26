from rest_framework import serializers
from .models import CarrerasModel


class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarrerasModel
        fields=('id','name','cantidad_ano','cantidad_asignaturas')
        
        
        