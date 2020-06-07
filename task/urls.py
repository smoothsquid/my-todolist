from django.urls import path
from task import views

urlpatterns = [
    path('', views.index, name='task.index'),
    path('add/', views.add, name='task.add'),
]
