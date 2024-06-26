from django import forms
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from users.models import AppUser

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
        fields = ["platform", "value"]


@require_GET
def view_page(request, username):
    """Renders the profile page for the given user. If the user exists but has
    no profile page, it will be created and then rendered."""
    page = Page.objects.filter(user__username=username).first()
    if not page:
        creator = AppUser.objects.filter(username=username)
        if creator.exists():
            page = Page.objects.create(user=creator.first())
            page.save()
        else:
            return HttpResponseNotFound()

    return render(
        request,
        "pages/view_page.html",
        {
            "page_data": page,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
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
@require_POST
def create_link(request):
    """Creates a link for the user's profile page with the data from the POST
    request."""
    user_page = Page.objects.get(user=request.user)
    new_link = PageLink(page_id=user_page.pk)

    form = PageLinkForm(request.POST, instance=new_link)
    if form.is_valid():
        form.save()
        return render(request, "pages/page_link_edit_view.html", {"link": new_link})
    else:
        return HttpResponse(form.errors.as_text())


@login_required
@require_http_methods(["DELETE"])
def delete_link(request, link_id):
    """Deletes the link with the ID specified in the path parameter."""
    link = PageLink.objects.get(pk=link_id)
    if link.page.user != request.user:
        return HttpResponseForbidden()

    link.delete()
    return HttpResponse()
