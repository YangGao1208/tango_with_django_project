from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/about/', views.about),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category')
    
]


