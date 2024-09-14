from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jose", views.jose, name="jose"),
    path("laura", views.laura, name="laura"),    
]
