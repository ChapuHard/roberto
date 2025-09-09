# filepath: c:\Users\SAMSUNG\Desktop\django\mi_proyecto\tareas\serializers.py
from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'nombre', 'precio']