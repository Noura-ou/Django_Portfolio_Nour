from django.urls import path
from . import views

app_name = "api_home"

urlpatterns = [
    
    path('', views.page_home, name ='home'),
   
]