from django.urls import path
from . import views

app_name = 'platillos'

urlpatterns = [
    path('', views.lista_platillos, name='lista_platillos'),
    path('nuevo/', views.platillo_new, name='platillo_new'),
    path('<int:pk>/editar/', views.platillo_edit, name='platillo_edit'),
    path('<int:pk>/eliminar/', views.platillo_delete, name='platillo_delete'),
    path('<int:platillo_pk>/receta/nueva/', views.receta_new, name='receta_new'),
    path('receta/<int:pk>/editar/', views.receta_edit, name='receta_edit'),
    path('receta/<int:pk>/', views.receta_view, name='receta_view'),
]
