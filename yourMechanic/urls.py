from django.urls import path,include
from . import views

urlpatterns = [
    path('api/fullbodypaint/', views.FullBodyPaintList.as_view()),

]