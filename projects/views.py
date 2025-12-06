from django.shortcuts import render
from . import models

# Create your views here.
def projects_view(request):
    # Logic to fetch and display projects
    projects_list = models.Project.objects.all()
    context = {'projects_list': projects_list}

    return render(request, 'projects/projects.html', context)