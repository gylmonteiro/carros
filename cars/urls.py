from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='listCars'),
    path('cadastrar_carro/', views.NewCarCreateView.as_view(), name='createCar'),
    path('cadastrar_marca/', views.CreateBrandView.as_view(), name='createBrand'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='carDetail'),
    path('<int:pk>/update/', views.CarUpdateView.as_view(), name='carUpdate'),
    path('<int:pk>/delete/', views.CarDeleteView.as_view(), name='carDelete')

]
