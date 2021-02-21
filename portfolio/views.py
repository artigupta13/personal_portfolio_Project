from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects=Project.objects.all()

    return render(request,'portfolio/home.html',{'projects':projects})

def portfolio(request,project_id):
    project=get_object_or_404(Project,pk=project_id)
    return render(request,'portfolio/portfolios.html',{'project':project})
