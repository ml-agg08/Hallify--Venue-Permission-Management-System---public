from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('venuefacultycoordinator_profile/',views.venuefacultycoordinator_profile,name='venuefacultycoordinator_profile'),
    path('VFCPermission_list/',views.VFCPermissionList,name='VFCPermissionList'),
    path('vfc_tag_edit/<pk>',views.VFCTagEdit,name='vfctagedit'),
    path('vfc_permission_details/<pk>',views.VFCPermissiondetails,name='vfc_permission_details')
]
