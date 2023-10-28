from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Receipe, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    #When the data comes from the front-end.
    if request.method == "POST":
        #For data and text.
        data = request.POST
        #For files and images.
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
       
       #To save the data in the models, imoprt models first
       #Then create it.
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    queryset = Receipe.objects.all()
    context = {"receipes": queryset}
    # print(queryset.receipe_name)
    return render(request, 'receipes.html', context)

#Let's create a delete functionality for the receipe.
def delete_receipe(request, id):
    #Here the all gives all the files and get gives according to desired one.
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect("/receipes/")
"""Exception argument is required in order to 
handle error page when exception eror occurs"""
def error404(request, exception):
    print("WORKING")
    return HttpResponse("OOPS NOT FOUND")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
        else:
            login(request,user)
            return redirect("/receipes/")

    return render(request, 'login.html')

def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already exists.")
            return redirect("/register")

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect("/register/")
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect("/login/")