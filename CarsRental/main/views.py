import secrets
import string
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(request:HttpRequest):

    return render(request, "main/home.html" )

def about_view(request:HttpRequest):
    return render(request,"main/about.html")

def password_view(request:HttpRequest):
    length = 10  
    characters = string.ascii_letters + string.digits + string.punctuation

    random_text = ''.join(secrets.choice(characters) for _ in range(length))
    return HttpResponse("The password: " + random_text)