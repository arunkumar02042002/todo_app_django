from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/addTask', views.addTask, name='addTask'),
    path('todo/markDone/<int:pk>/', views.markDone, name='markDone'),
    path('todo/deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('todo/markUndone/<int:pk>/', views.markUndone, name='markUndone'),
    path('todo/editTask/<int:pk>/', views.editTask, name='editTask'),
]