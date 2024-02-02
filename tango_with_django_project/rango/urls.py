from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about)
    
]


