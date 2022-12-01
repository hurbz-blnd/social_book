from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.

#@login_required(login_url= "signin")
def index(request):
    return render(request, template_name= 'index.html' )

def signup(request):

    if request.method == "POST":
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Password2 = request.POST['Password2']
        
        if Password == Password2:
            if User.objects.filter(email= Email).exists():
                messages.info(request, "Email already exists, lil dum..")
                return redirect('signup')
            elif User.objects.filter(username= Username).exists():
                messages.info(request, "That username is taken, lil dum..")
                return redirect('signup')
            else:
                user = User.objects.create_user(username= Username, email= Email, password= Password)
                user.save()

                #Log user in and redirect to settings page
                user_login = authenticate(username= Username, password= Password)
                login(request, user_login)

                #Create a Profile object the new user 
                user_model= User.objects.get(username= Username)
                user_profile = Profile.objects.create(user= user_model, ID_user= user_model.id)
                user_profile.save()
                
                return redirect('setting') #Update this to 'login' template when one is made

        else:
            messages.info(request, "Passwords do not match, lil dum..")
            return redirect('signup')

    else:
        return render(request,template_name= 'signup.html')


#@login_required(login_url= "signin")
def signin(request):
    if request.method == "POST":
        userN= request.POST['username']
        passWD= request.POST['password']

        user = authenticate(username= userN, password= passWD)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('signin')
    
    else:
        return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect('signin')

#@login_required(login_url= "signin")
def setting(request): 
    user_profile= Profile.objects.get(user= request.user)


    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileImg
            bio = request.POST['bio']
            location = request.POST['location'] 

            user_profile.profileImg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        elif request.FILES.get('image') != None:
            image= request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location'] 

            user_profile.profileImg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('setting')



    return render(request, 'setting.html', {'user_profile': user_profile})