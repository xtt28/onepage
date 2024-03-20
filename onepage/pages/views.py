from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Page


def view_page(request, username):
    """Renders the profile page for the given user."""
    page_data = Page.objects.filter(user__username=username).first()
    print(page_data)
    if not page_data:
        return HttpResponseNotFound()
    return render(
        request,
        "pages/view_page.html",
        {
            "page_data": page_data,
        },
    )
