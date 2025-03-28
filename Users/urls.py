from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.account,name='account'),
    path('account/',views.account,name='account'),
    path('usertype/',views.usertype,name='usertype'),
    path('logout/',views.logout,name='logout'),
    path('firstpage/',views.firstpage,name='firstpage'),
    path('showprofile/',views.show_profile,name='showprofile'),
    path('about/',views.about,name='about')
]