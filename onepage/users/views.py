from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    """Renders a dashboard with links for authenticated users to manage their
    profiles."""
    return render(request, "users/dashboard.html")
