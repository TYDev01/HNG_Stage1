from django.urls import path
from . import views

# My urls goes in below

urlpatterns = [
    path("api/hello", views.newVisitor, name='newuser')
]
