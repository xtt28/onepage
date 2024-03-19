from django.shortcuts import render

def view_page(request, username):
    """"""
    return render(request, "pages/view_page.html")
