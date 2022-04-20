
from django.urls import path,include
from . import views

urlpatterns = [
    path('api/fullbodypaint/', views.FullBodyPaintList.as_view()),
    path('api/stereosetup/', views.StereoSetupList.as_view()),
    path('api/enginerepair/', views.EngineRepairList.as_view()),
    path('api/customer/', views.CustomerList.as_view()),
    path('api/mechanic/', views.MechanicList.as_view()),

]

