from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from Account.forms import LoginForm


# Create your views here.
'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnianie zakończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane')


    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
'''

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard'})