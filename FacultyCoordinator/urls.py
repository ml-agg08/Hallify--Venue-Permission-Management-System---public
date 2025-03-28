from django.urls import path
from . import views

urlpatterns=[
        path('facultycoordinator_profile/',views.facultycoordinator_profile,name='facultycoordinator_profile'),
        path('fc_permission_list/',views.FCPermissionList,name='FCPermissionList'),
        path('fc_tag_edit/<pk>',views.FCTagEdit,name='fctagedit'),
        path('fc_permission_details/<pk>',views.FCPermissiondetails,name='fc_permission_details')
]