from django.contrib.auth.models import User
from django.shortcuts import render,  redirect
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *

# Create your views here.


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'Home/index.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('cards:CardsProjects_All')
        return HttpResponse('<p>bhag</p>')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Home/registrationform.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            u = Usersinfo()
            us = User.objects.get(pk=user.pk)
            u.no = us
            u.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cards:CardsProjects_All')
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('Home:welcome')


def board(request):
    return render(request, 'Home/base.html', {})
