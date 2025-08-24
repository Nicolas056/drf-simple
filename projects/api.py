from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    # veremos que tipo de consultas se podran realizar
    # en este caso son todos los objetos asociados al modelo llamado Project
    queryset = Project.objects.all()
    # ahora veremos los permisos
    # en este caso cualquier aplicacion cliente podra solicitar informacion en el servidor
    # si queremos que la persona este autenticada seria: (IsAuthenticated)
    permission_classes = [permissions.AllowAny]
    # ahora diremos a partir de qie serializer estara viendo los datos
    # es decir, como lo va a convertir
    serializer_class = ProjectSerializer
