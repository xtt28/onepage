from django.urls import path
from .views import user_settings

urlpatterns = [
    path("you", user_settings, name="user_settings"),
]
