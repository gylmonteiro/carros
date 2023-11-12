from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='listCars'),
    path('cadastrar_carro/', views.CreateCarView.as_view(), name='createCar'),
    path('cadastrar_marca/', views.CreateBrandView.as_view(), name='createBrand')

]
