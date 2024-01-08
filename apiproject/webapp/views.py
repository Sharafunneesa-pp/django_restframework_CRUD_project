from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import CreateView,FormView,View,TemplateView
from webapp.forms import LoginForm,RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



class RegistrationView(CreateView):
    form_class=RegistrationForm
    model=User
    template_name="register.html"
    success_url=reverse_lazy("signin")


class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args:str,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
        else:
            return render(request,self.template_name,{"form":form})
        


class IndexView(TemplateView):
    template_name="home.html"
    form_class=LoginForm
        
