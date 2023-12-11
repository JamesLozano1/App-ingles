from rest_framework import serializers
from .models import Materia, Tarea

class MateriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Materia
        fields = '__all__'


class TareaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'