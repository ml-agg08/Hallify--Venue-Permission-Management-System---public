from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list,name="permission_list"),
    path('permission_details/<pk>',views.permission_details,name='permission_details'),
    path('create_permission/',views.create_permission,name="create_permission")
]