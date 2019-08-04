from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm

def create(request):
    """Root view, which will be display, when the user
    will try to sign up"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:index')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/create_account.html', {'form': form})

@login_required
def account(request):
    """ Method for my_account page"""
    return render(request, 'accounts/my_account.html')

