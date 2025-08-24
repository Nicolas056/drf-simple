# djnago rest te da una opcion para hacer las rutas de forma automatica
from rest_framework import routers
from .api import ProjectViewSet

# de esta forma creamos el crud
router = routers.DefaultRouter()
# registramos la ruta
router.register('api/projects', ProjectViewSet, 'projects')
# ahora lo exportamos
urlpatterns = router.urls
