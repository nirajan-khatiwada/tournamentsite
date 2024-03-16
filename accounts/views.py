from django.shortcuts import render,redirect
from .forms import Register,Login,Fopass,Activate
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login,logout,authenticate
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method=="GET"):
        form=Register()
        return render(request,"accounts/register.html",{"data":form})
    if(request.method=="POST"):
        form=Register(request.POST)
        if form.is_valid():
            if(form.cleaned_data.get("password")==form.cleaned_data.get("confirm_Password")):
                form.save()
                return redirect("login")
            else:
                messages.error(request,"Password Doesnt match should be same")
                return render(request,"accounts/register.html",{"data":form})

        else:
            User=get_user_model()
            if User.objects.filter(username=form.cleaned_data.get("username")).exists:
                messages.error(request,"Username Already Exists")
                return render(request,"accounts/register.html",{"data":form})

            messages.error(request,"Enter All The Fields")
            return render(request,"accounts/register.html",{"data":form})


def Logins(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method=="GET":
        form=Login()
        for x in form:
            print(x)
        return render(request,"accounts/login.html",{'form':form})
    elif request.method=="POST":
        print(request.POST)
        form=Login(request.POST)
    
        if form.is_valid():
            user=authenticate(username=form.cleaned_data.get("username"),password=form.cleaned_data.get("password"))
            if user is None:
                messages.error(request,"Invalid Credientials")
                return redirect("login")
            
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Enter Both Of The Fields")
            return redirect("login")


def Logouts(request):   
    logout(request)
    messages.success(request,"Logout Sucessfully")
    return redirect("login")

def Fpass(request):
    if request.method=="GET":
       form=Fopass()
       return render(request,"accounts/Fpass.html",{'form':form})
    
    if request.method=="POST":
        form=Fopass(request.POST)
        if form.is_valid():
            User=get_user_model()
            user=User.objects.filter(email=form.cleaned_data.get("email"))
            if user.exists():
                token=default_token_generator.make_token(user.first())
                print(user.first())
                
                html=render_to_string("accounts/email.html",{'host':request.META.get("HTTP_HOST"),'request':request,'token':token,'username':user.first().username})

                email=EmailMultiAlternatives("RESET YOUR PASSWORD",token,"no reply<usa.nirajankhatiwada29@gmail.com>",[form.cleaned_data.get("email")])
                email.attach_alternative(html,"text/html")
                email.send()
                messages.success(request,"Email send.Please check your email")
                return redirect("login")

            else:
                messages.error(request,"No Email Registered")


        else:
            messages.error(request,"Please input email")
        return redirect("forgot")

def activate(request):
    if request.method=="GET":
        form=Activate(request.GET)
        if form.is_valid():
           User=get_user_model()
           user=User.objects.filter(username=form.cleaned_data.get("username"))
           token=form.cleaned_data.get("token")
           is_valid=default_token_generator.check_token(user,token)
           if is_valid:

        else:
            messages.error("Forgot Password Unsucessful")
            
            return redirect("forgot")

    