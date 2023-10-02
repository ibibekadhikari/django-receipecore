from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Receipe

# Create your views here.
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

    return render(request, 'receipes.html')

"""Exception argument is required in order to 
handle error page when exception eror occurs"""
def error404(request, exception):
    print("WORKING")
    return HttpResponse("OOPS NOT FOUND")