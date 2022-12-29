from django.urls import path,include
from .import views

urlpatterns = [
    #path("",views.index,name='index'),
    path("ca9e9764-9e0d-4318-9d6d-9b6180d195f4/",views.WebHookSetUp,name=" WebHookSetUp")
   
]
