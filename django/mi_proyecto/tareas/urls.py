from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet  # Cambiado a importación relativa

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]