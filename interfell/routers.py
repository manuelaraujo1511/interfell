from rest_framework import routers
from papp.viewsets import UsuariosViewSet

router = routers.DefaultRouter()

router.register(r'user', UsuariosViewSet)