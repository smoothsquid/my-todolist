from django.urls import path
from task import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('done/<int:pk>/', views.done, name='done'),
    path('incomplete/<int:pk>/', views.incomplete, name='incomplete'),
]
