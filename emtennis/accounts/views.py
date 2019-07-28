from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm

def create(request):
    """Root view, which will be display, when the user
    will try to sign up"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome:home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/create_account.html', {'form': form})


