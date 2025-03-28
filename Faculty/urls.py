from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("faculty_profile/",views.faculty_profile,name="faculty_profile"),
    path("facpermissionlist/",views.FACPermissionList,name="FACPermissionList"),
    path('fac_create_permission/',views.fac_create_permission,name="fac_create_permission"),
    path('fac_permission_details/<pk>',views.fac_permission_details,name='fac_permission_details')
]

