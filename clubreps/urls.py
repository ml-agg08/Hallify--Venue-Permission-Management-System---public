from django.urls import path
from . import views

urlpatterns=[
        path('clubrep_profile/',views.clubrep_profile,name='clubrep_profile')
]