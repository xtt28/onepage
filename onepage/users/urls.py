from django.urls import path
from .views import dashboard

urlpatterns = [path("you", dashboard, name="dashboard")]
