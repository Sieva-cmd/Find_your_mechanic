from django.urls import path, include
from . import views
from .views import RegisterList

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),

    path('home/', views.home, name='home'),

    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('mechanic/', views.mechanic, name='mechanic'),

    path('api/register/', RegisterList.as_view(), name='register'),

]