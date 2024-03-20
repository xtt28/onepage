from django.urls import path
from .views import view_page

urlpatterns = [path("@<username>", view_page)]
