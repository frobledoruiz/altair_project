from django.shortcuts import render
from contractors.models import Contractor

from projects.models import Project
from projects.choices import scope_choices, state_choices

def index(request):
    projects = Project.objects.order_by('-create_date').filter(is_published=True)[0:3]

    context = {
        'projects': projects,
        'scope_choices': scope_choices,
        'state_choices': state_choices   
    }
    return render(request, 'pages/index.html', context)
