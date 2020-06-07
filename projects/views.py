from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, 'projects/home.html',{'projects':projects})
