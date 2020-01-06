from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="logger-landing"),
    path('dashboard/', views.dashboard, name="logger-dashboard"),

]
