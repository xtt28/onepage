from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Page


def view_page(request, username):
    """Renders the profile page for the given user."""
    page_data = get_object_or_404(Page, user__username=username)
    return render(
        request,
        "pages/view_page.html",
        {
            "page_data": page_data,
        },
    )


@login_required
def edit_page(request):
    """Renders a view that allows a user to modify their profile page."""
    return render(request, "pages/edit_page.html")
