from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tareas.urls')),  # Esto conecta con las URLs de la app tareas
]