
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    re_path(r'^api/fullbodypaint/$', views.FullBodyPaintList.as_view()),
    re_path(r'^api/stereosetup/$', views.StereoSetupList.as_view()),
    re_path(r'^api/enginerepair/$', views.EngineRepairList.as_view()),
    re_path(r'^api/customer/$', views.CustomerList.as_view()),
    re_path(r'^api/mechanic/$', views.MechanicList.as_view()),

]

