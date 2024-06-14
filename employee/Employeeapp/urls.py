from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path('home', views.index, ),
    path('create', views.create_view, ),
    path('display', views.retrieve_view, ),
    path('delete/<int:did>', views.delete_view, ),
    path('update/<int:uid>', views.update_view, ),
)