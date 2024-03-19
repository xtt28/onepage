from django.urls import include, path
from .views import view_page

urlpatterns = [
    path('<username>', view_page)
]
