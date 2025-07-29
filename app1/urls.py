from django.urls import path
from .views import app1_view

urlpatterns = [
    path("", app1_view),
]