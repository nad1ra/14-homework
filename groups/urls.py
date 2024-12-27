from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.group_list, name='list'),
    path('add/', views.group_add, name='add'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
    path('delete/<int:pk>/', views.track_delete, name='delete'),
]
