from django.urls import path
from .views import edit_page, view_page

urlpatterns = [path("@<username>", view_page), path("edit", edit_page)]
