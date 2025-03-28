from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("security_profile/",views.security_profile,name="security_profile"),
    path("scypermissionlist/",views.SCYPermissionList,name="SCYPermissionList"),
    path("scypermissiondetails/<pk>",views.SCYPermissionDetails,name="SCYPermissionDetails"),
    path("scytagedit/<pk>",views.SCYTagEdit,name="scytagedit")
]

