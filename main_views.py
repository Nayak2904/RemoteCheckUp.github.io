from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import  View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
import random
from .models import * 


#============================================================================================
#======================================= Login Page =========================================

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        value = {
          'email' : email,
        }
        error_message = None
        
        user = User.objects.filter(email=email)
        for u in user:
          user_password=u.password
          flag = check_password(password,user_password)
        if user:
          if flag:
                    request.session['email']=request.POST["email"]
                    return redirect('index')
          else:
                    error_message = 'Password is invalid !!'
        else: 
            error_message = "Email is Invalid !!"

        return render(request, 'login.html', {'error':error_message,'value':value})
#===========================================================================================
#============================================================================================




#=================================== Signup =================================================

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method=="POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            value = {
                'first_name':first_name,
                'last_name':last_name,
                'username':username,
                'email':email,

            }
            error_message = None
            user = User(
                              first_name=first_name,
                              last_name=last_name,
                              email=email,
                              username=username,
                              password=password
            )
            if(not first_name ):
                error_message = "Fisrt Name is Required !!"
            elif not last_name:
                error_message = "Last Name is Required !!"
            elif not email:
                error_message = "Email Address is Required !!"
            elif not username:
                error_message = "Username is Required !!"
            elif not password:
                error_message = "Password is Required !!"
            if not error_message:
                user.password = make_password(user.password)
                user.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('login')
                
                
            else:
                data = {
                'error' : error_message,
                'value' : value 
            }
            return render(request, 'signup.html', data)
#============================================================================================
#============================================================================================




#======================================== Logout Page =======================================

def dologout(request):
    if request.session.has_key('email'):
        del request.session["email"]
        return redirect('login')
    else:
        return redirect('login')

#============================================================================================
#============================================================================================




#==================================== Index ==================================================

def index(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        user = User.objects.get(email=email)
        data = {
            'user':user,
        }
        return render(request,'base.html',data)
    else:
        return redirect('login')

#=============================================================================================
#=============================================================================================




#===================================== Contact ===============================================

def contact(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        user = User.objects.get(email=email)
        data = {
            'user':user,
        }
        if request.method=="POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            Contact(
                name = name,
                email = email,
                subject = subject,
                message = message
            ).save()
            messages.success(request, 'Thanks For Contacting')
            return render(request,'base.html',data)
    else:
        return redirect('login')
#============================================================================================
#============================================================================================



#=========================================== Report ==========================================

def report(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        user = User.objects.get(email=email)
        if request.method=="POST":
            your_name = request.POST.get("your_name")
            gender = request.POST.get("gender")
            phone = request.POST.get("phone")
            age = request.POST.get("age")
            height = request.POST.get("height")
            weight = request.POST.get("weight")
            smoke = request.POST.get("smoke")
            diabetes = request.POST.get("diabetes")
            blood_presure = request.POST.get("blood_presure")
            heart_rate = request.POST.get("heart_rate")
            ldl = request.POST.get("ldl")
            hdl = request.POST.get("hdl")
            state = request.POST.get("state")
            ldl2 = int(ldl)
            hdl2 = int(hdl)
            center = Health.objects.filter(state = state)
            
            if ldl2 < 70 and hdl2 > 40:
                list1 = [1, 2, 3, 4]
                heart_attact1 = random.choice(list1)
                risk = 'Low'
            else:
                list2 = [5,6,7,8,9,10]
                heart_attact1 = random.choice(list2)
                risk = 'High'
            data = {
                'your_name':your_name,
                'gender':gender,
                'phone':phone,
                'age':age,
                'height':height,
                'weight':weight,
                'smoke':smoke,
                'diabetes':diabetes,
                'blood_presure':blood_presure,
                'heart_rate':heart_rate,
                'ldl':ldl,
                'hdl':hdl,
                'heart_attact1':heart_attact1,
                'risk':risk,
                'center':center,
                'user':user,
            }
            return render(request,'report.html',data)
    else:
        return redirect('login')
#============================================================================================
#============================================================================================




#===================================== Book Appointment ========================================

def book_appointment(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        user = User.objects.get(email=email)
        data = {
            'user':user,
        }
        if request.method=="POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            service = request.POST.get("service")
            doctor = request.POST.get("doctor")
            date = request.POST.get("date")
            time = request.POST.get("time")
            Appointment(
                user = user,
                name = name,
                number = phone,
                service = service,
                doctor = doctor,
                date = date,
                time = time
            ).save()
            messages.success(request, 'Your Appointment Book Successfully')
            return redirect('appointment')
    else:
        return redirect('login')


#============================================================================================
#============================================================================================




#===================================== Appointment ===========================================

def appointment(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        user = User.objects.get(email=email)
        appointment = Appointment.objects.filter(user=user)
        data = {
            'user':user,
            'appointment':appointment,
        }
        return render(request,'appointment.html',data)
    else:
        return redirect('login')


#============================================================================================
#============================================================================================
