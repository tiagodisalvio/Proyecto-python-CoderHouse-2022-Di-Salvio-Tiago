from django.shortcuts import render

# Create your views here.

def homepage(req):
 return render(req, 'homepage/index.html')

def about(req):
 return render(req, 'homepage/about.html')
 