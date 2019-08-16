from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm, ProfileForm
from django.http import HttpResponse

def create(request):
    """Root view, which will be display, when the user
    will try to sign up"""
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('events:index')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/create_account.html', {'user_form': user_form,
                                                            'profile_form': profile_form})

@login_required
def account(request):
    """ Method for my_account page"""
    user = request.user
    registrations = user.profile.registration_set.all()
    return render(request, 'accounts/my_account.html', {'registrations':registrations})

def matchmaking(request):
    """ Function to define a page under construction """
    return HttpResponse("Fonctionnalité en cours de construction...")