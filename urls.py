from django.urls import path
from . import views
from .views import ProtectedView


urlpatterns = [
    path('', views.index, name='index'),
    path('denuncias/', views.lista_denuncias, name='lista_denuncias'),
    path('denuncias/nova/', views.nova_denuncia, name='nova_denuncia'),
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
    
    
]
