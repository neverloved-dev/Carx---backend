# Uncomment next two lines to enable admin:
#from django.contrib import admin
from django.urls import path
from .views import register_api,test_api

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('register',register_api),
    path('test',test_api)
]