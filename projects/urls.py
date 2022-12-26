# rest da un modulo que crea todas las rutas o crud de los datos
from rest_framework import routers
from .api import ProjectViewSet

#crea el crud en una variable
router = routers.DefaultRouter()

#usando la ruta se registra | se importa projectviewset y se coloca nombre a la ruta
router.register('api/projects', ProjectViewSet, 'projects')

# Genera las urls, POST, PUT, DELETE, GET y manejas las peticiones 
urlpatterns = router.urls


