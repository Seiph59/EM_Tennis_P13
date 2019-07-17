from django.shortcuts import render

def index(request):
    """Root view, which will be display, when the user
    will try to access to the website. Events are display on this page"""
    return render(request, 'events/index.html')
