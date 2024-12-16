from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import CustomSignUpForm


class SignUp(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return HttpResponseRedirect(request, '/accounts/logout')


