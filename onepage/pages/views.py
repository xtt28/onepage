from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import get_object_or_404, render
from django import forms
from .models import Page, PageLink


class PageForm(forms.ModelForm):
    """A form that allows the user to update settings about their page."""

    class Meta:
        model = Page
        fields = ["description"]


class PageLinkForm(forms.ModelForm):
    """A form that allows the user to update or create a link for their page."""

    class Meta:
        model = PageLink
        fields = ["url"]


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
    page, _ = Page.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/@{request.user.username}")
    else:
        form = PageForm(instance=page)
        link_form = PageLinkForm()
    return render(
        request, "pages/edit_page.html", {"form": form, "link_form": link_form}
    )


@login_required
def create_link(request):
    """Creates a link for the user's profile page with the data from the POST
    request."""
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])

    user_page = Page.objects.get(user=request.user)
    new_link = PageLink(page_id=user_page.pk)

    form = PageLinkForm(request.POST, instance=new_link)
    if form.is_valid():
        form.save()
        return HttpResponse("Link added")
    else:
        return HttpResponse(form.errors.as_text())
