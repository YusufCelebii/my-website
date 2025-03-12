from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"portfolio_app/home.html")

def blog(request):
    return render(request,"portfolio_app/blog.html")

def projects(request):
    return render(request,"portfolio_app/projects.html")

