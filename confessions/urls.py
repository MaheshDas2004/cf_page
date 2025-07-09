from django.urls import path
from . import views

urlpatterns = [
    path('confessions/', views.confessions, name='confession'),
    path('submit_confessions/', views.submit_confession, name='submit_confession'),
    
]