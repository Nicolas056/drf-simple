from rest_framework import serializers
from .models import Project

# cuando se haga alguna peticion, se sabe que se hara a la bd asociada a ese nombre
# en este caso el modelo que se llama Project


class ProjectSerializer(serializers.ModelSerializer):
    # esto convierte el modelo en datos que pueden ser consultados por el cliente
    class Meta:
        # colocamos el nombre del modelo
        model = Project
        # colocamos los campos que queremos que sean consultados
        fields = ('id', 'title', 'description', 'technology', 'created_date')
        # colocamos los campos que son solo de lectura
        # datos que solo se leeran y que no se pueden modificar
        read_only_fields = ('created_date', )
