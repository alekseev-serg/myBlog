from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.get_category, name='category')
]
