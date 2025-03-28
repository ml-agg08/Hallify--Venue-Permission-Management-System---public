from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("venuefacultystaff_profile/",views.VenueFacultyStaffProfile,name='venuefacultystaff_profile'),
    path("vfspermissionlist/",views.VFSPermissionList,name="VFSPermissionList"),
    path('vfs_permission_details/<pk>',views.VFSPermissiondetails,name='vfs_permission_details')
]

