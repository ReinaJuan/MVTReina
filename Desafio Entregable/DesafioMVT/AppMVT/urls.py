
from django.urls import path
from AppMVT import views
from .views import *






urlpatterns = [
path("familiares/", familiares, name= "familiares"),
    
]