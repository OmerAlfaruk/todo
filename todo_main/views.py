from django.shortcuts import render


def home(request):
    """
    Home view that renders the home page.
    """
    return render(request, "home.html")
