from django.urls import path
from .views import edit_page, view_page, create_link, delete_link

urlpatterns = [
    path("@<str:username>", view_page, name="view_page"),
    path("edit", edit_page, name="edit_page"),
    path("edit/links", create_link, name="create_link"),
    path("edit/links/delete/<int:link_id>", delete_link, name="delete_link"),
]
