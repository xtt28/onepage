from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.shortcuts import redirect, render


@login_required
@require_GET
def user_settings(request):
    """Renders a page showing available settings for the user to configure their
    account."""
    return render(request, "users/settings.html")


@login_required
@require_GET
def delete_user(request):
    """Renders a page that confirms whether the user would like to delete their
    account."""
    return render(request, "users/delete_confirm.html")


@login_required
@require_GET
def delete_final(request):
    """Deletes the user's account permanently."""
    request.user.delete()
    return redirect("login")


@login_required
def logout_view(request):
    """Logs the user out of their active session."""
    logout(request)
    return redirect("login")
