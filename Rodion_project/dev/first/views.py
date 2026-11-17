from django.shortcuts import render
from .models import Project, Skill, Experience

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    context = {
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
    }
    return render(request, 'index.html', context)