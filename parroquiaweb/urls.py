from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catequesis.urls')),  # Esto importa todas las rutas de catequesis
]
