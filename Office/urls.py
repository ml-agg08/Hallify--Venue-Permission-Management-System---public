from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("office_profile/",views.office_profile,name="office_profile"),
    path("offpermissionlist/",views.OFFPermissionList,name="OFFPermissionList"),
    path("offpermissiondetails/<pk>",views.OFFPermissionDetails,name="OFFPermissionDetails"),
    path("offtagedit/<pk>",views.OFFTagEdit,name="offtagedit")
]

