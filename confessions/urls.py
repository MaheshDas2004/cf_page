from django.urls import path
from . import views

urlpatterns = [
    path('confessions/', views.confessions, name='confession'),
    
]