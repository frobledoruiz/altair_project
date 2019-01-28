from django.shortcuts import render
from contractors.models import Contractor

from projects.models import Project

def index(request):
    projects = Project.objects.order_by('-create_date').filter(is_published=True)[0:3]

    context = {
        'projects': projects,
    }
    return render(request, 'pages/index.html', context)
