from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]