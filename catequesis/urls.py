from django.urls import path
from . import views

app_name = 'catequesis'  # ⬅️ Esto activa el uso de namespaces en los templates

urlpatterns = [
    path('registrar/', views.registrar_catequizando, name='registrar_catequizando'),
    path('listar/', views.listar_catequizandos, name='listar_catequizandos'),
    path('todos/', views.listar_todos_catequizandos, name='listar_todos_catequizandos'),
    path('modificar/<int:id>/', views.modificar_catequizando, name='modificar_catequizando'),
    path('eliminar/<int:id>/', views.eliminar_catequizando, name='eliminar_catequizando'),
    path('catequistas/', views.listar_catequistas, name='listar_catequistas'),
    path('catequistas/registrar/', views.registrar_catequista, name='registrar_catequista'),
    path('catequistas/modificar/<int:id>/', views.modificar_catequista, name='modificar_catequista'),
    path('catequistas/eliminar/<int:id>/', views.eliminar_catequista, name='eliminar_catequista'),
]
