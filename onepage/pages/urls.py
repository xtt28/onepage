from django.urls import path
from .views import edit_page, view_page, create_link

urlpatterns = [
    path("@<username>", view_page, name="view_page"),
    path("edit", edit_page, name="edit_page"),
    path("edit/links", create_link, name="create_link"),
]
