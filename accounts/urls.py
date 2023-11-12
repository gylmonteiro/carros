from django.urls import path
from . import views

urlpatterns = [
    path('criar_usuario/', views.create_user_view, name='create_user'),
    path('entrar/',views.login_view, name='login_user'),
    path('sair/', views.logout_view, name='logout_user'),
]
