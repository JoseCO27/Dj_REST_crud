from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
# clase que hereda desde viewsets para ver que consultas se pueden realizar

class ProjectViewSet(viewsets.ModelViewSet):
    # que consultas se pueden hacer
    queryset = Project.objects.all()
    # se dice en una clase: quien tiene permitido hacer operaciones
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

