from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView , LogoutView , PasswordResetView ,PasswordResetDoneView ,PasswordResetConfirmView ,PasswordResetCompleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.models import User


from .forms import RegisterForm


class PasswordResetDoneInterfaceView(PasswordResetDoneView):
    template_name ='home/reset_password_done.html'

class PasswordResetCompleteInterfaceView(PasswordResetCompleteView):
    template_name = 'home/password_reset_complete.html'

class PasswordResetConfirmInterfaceView(PasswordResetConfirmView):
    template_name ='home/password_reset_confirm.html'

class PasswordResetInterfaceView(PasswordResetView):
    template_name = 'home/password_reset.html'

class RegisterView(FormView):
    template_name = 'home/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(RegisterView, self).form_valid(form)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
   template_name = 'home/login.html'
   redirect_authenticated_user=True
   

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today' : datetime.today()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
