from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    """A form that allows the user to update settings about their page."""

    class Meta:
        model = Page
        fields = ["description"]


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
    """If the request method is GET, renders a view that allows a user to modify
    their profile page. If the method is POST, accepts a PageForm to update the
    user's profile page."""
    page = Page.objects.get(user=request.user)

    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/@{request.user.username}")
    else:
        form = PageForm(instance=page)
    return render(request, "pages/edit_page.html", {"form": form})
