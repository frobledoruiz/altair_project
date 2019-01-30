from django.shortcuts import render

from contractors.models import Contractor
from projects.choices import budget_choices, scope_choices, state_choices, goaltime_choices
from projects.models import Project


def index(request):
    projects = Project.objects.order_by('-create_date').filter(is_published=True)[0:3]

    context = {
        'projects': projects,
        'scope_choices': scope_choices,
        'state_choices': state_choices,
        'budget_choices': budget_choices,
        'goaltime_choices': goaltime_choices 
    }
    return render(request, 'pages/index.html', context)
