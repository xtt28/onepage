from django.urls import path
from .views import delete_final, delete_user, logout_view, user_settings

urlpatterns = [
    path("you", user_settings, name="user_settings"),
    path("you/delete", delete_user, name="delete_user"),
    path("you/delete/final", delete_final, name="delete_final"),
    path("you/logout", logout_view, name="logout"),
]
