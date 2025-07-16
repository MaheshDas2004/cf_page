from django.urls import path
from . import views

urlpatterns = [
    path('confessions/', views.confessions, name='confession'),
    path('my_confessions/', views.my_confessions, name='my_confession'),
    path('submit_confessions/', views.submit_confession, name='submit_confession'),
    path('delete_confession/<int:id>/', views.delete_confession, name='delete_confession'),
    # path('edit_confession/<int:id>/', views.edit_confession, name='edit_confession'),

]