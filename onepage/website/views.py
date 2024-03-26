from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home(request):
    """Renders a page describing the application."""
    return render(request, "website/home.html")
