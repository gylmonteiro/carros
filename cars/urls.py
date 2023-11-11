from django.urls import path
from . import views

urlpatterns = [
    path('', views.carviews, name='listCars'),
    path('cadastrar_carro/', views.create_car_views, name='createCar'),
    path('cadastrar_marca/', views.create_brand_views, name='createBrand')

]
