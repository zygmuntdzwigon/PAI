from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='debt-home'),
    path('about/', views.about, name="debt-about"),
]