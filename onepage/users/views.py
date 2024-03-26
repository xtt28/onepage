from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.shortcuts import render


@login_required
@require_GET
def user_settings(request):
    return render(request, "users/settings.html")
