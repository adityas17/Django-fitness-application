from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate 
from django.db import IntegrityError
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Project.objects.all()
    return render(request,"generator/home.html", {'projects':projects})

@login_required
def bmr_output(request):
    if request.method == 'GET':
        return render(request, "generator/bmr_output.html")
    else:
         data = request.POST
         print("hii")
         print(data) 
         weight = int(data["weight"])
         height = int(data['height'])
         age = int(data["age"])
         wf = int(data['length'])
         print(type(age))
         if request.POST['gender'] == 'male':
            # data["age"]
            answer = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age) 
            if wf == 5:
                answer = answer*(1)
            elif wf == 6:
                answer = answer*(1.3)
            elif wf == 7:
                answer = answer*(1.5)
            else:
                answer = answer*(1.7)
         if request.POST['gender'] == 'female':
            answer = 655.1 + (9.563*weight) + (1.85*height) - (4.676+age)
         answer = int(abs(answer))
         print(type(answer))
    return redirect ('bmr', answer)

@login_required
def bmr(request, answer):
    newobject = Bmr_result(user=request.user,output=answer)
    # newobject = Bmr_result.objects.create()
    # newobject.user = request.user
    # newobject.output = answer
    newobject.save()
    return render(request, "generator/bmr.html", {"bmr" : answer})

@login_required
def bmi_output(request):
    if request.method == 'GET':
        return render(request, "generator/bmi_output.html")
    else:
         data = request.POST
         print("hii")
         print(data) 
         weight = int(data["weight"])
         height = int(data['height'])*0.01
         print(height)
         heightw = height * height
         newans = weight/heightw
         newans= int(abs(newans))
         print(newans)
    return redirect ('bmi', newans)

@login_required
def bmi(request, newans):
    newobject2 = Bmi_result(user=request.user,output=newans)
    newobject2.save()
    return render(request,"generator/bmi.html",{"bmi" : newans})

def signupuser(request):
    if request.method == 'GET':
        return render(request,'generator/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'generator/signupuser.html',{'form':UserCreationForm(), 'error':'Username already taken, Try again'})
        else:
            return render(request,'generator/signupuser.html', {'form': UserCreationForm(),'error':'Passwords did not match '} )


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method =='GET':
        return render(request,'generator/loginuser.html',{'form':AuthenticationForm()}) 
    else:
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request,'generator/loginuser.html',{'form':AuthenticationForm(), 'error':'Such account does not exist'})
        else:
            login(request,user)
            return redirect('home') 

def tableuser(request):
    results= Bmr_result.objects.filter(user = request.user)
    results2= Bmi_result.objects.filter(user = request.user)
    return render(request,'generator/tableuser.html',{'results': results, 'results2':results2})














