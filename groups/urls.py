from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.groups_list, name='list'),
    path('create/', views.group_create, name='create'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
    path('update/<int:pk>/', views.group_update, name='update'),
    path('delete/<int:pk>/', views.group_delete, name='delete'),
]
