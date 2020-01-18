from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="logger-landing-page"),
    path('dashboard/', views.dashboard, name="logger-dashboard"),
    path('log-workout/', views.log_workout, name="logger-log-workout"),
    path('log-history/', views.logged_sessions, name="logger-logged-sessions"),
    path('save-workout/', views.save_workout, name="logger-save-workout")
]
