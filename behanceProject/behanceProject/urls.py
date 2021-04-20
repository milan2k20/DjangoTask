from django.contrib import admin
from django.urls import path
from behanceApp.Views import information, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', information.InformationView.as_view(), name ='home'),
    path('search/', search.GetInformation.as_view(), name ='search')
]
