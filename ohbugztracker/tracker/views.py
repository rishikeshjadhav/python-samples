from django.shortcuts import render
from .models import Project, Task
from .forms import ProjectForm
from django.shortcuts import redirect

# Create your views here.


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def add_new_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            p = Project.objects.create(title=title, description=description)
            if p.pk > 0:
                return redirect('index')
    return render(request, 'project/add.html', {'form': form})


def myview(request):
    employees = [
        {
            'Name': 'User One',
            'EmpId': 'EMP001',
            'Designation': 'CEO'
        },
        {
            'Name': 'User Two',
            'EmpId': 'EMP002',
            'Designation': 'Vice President'
        }
    ]
    return render(request, 'myview.html', {'employees': employees})
