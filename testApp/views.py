from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import signUp
from django.http import HttpResponseRedirect
# Create your views here.
def home_view(request):
    return render(request,"testApp/home.html")

@login_required
def java_view(request):
    return render(request,"testApp/javaexam.html")

@login_required
def python_view(request):
    return render(request,"testApp/pythonexam.html")

@login_required
def apti_view(request):
    return render(request,"testApp/aptiexam.html")

def logout_view(request):
    return render(request,"testApp/logout.html")

def signup_view(request):
    forms=signUp()
    if(request.method=='POST'):
        forms=signUp(request.POST)
        user=forms.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,"testApp/signup.html",{"forms":forms})
