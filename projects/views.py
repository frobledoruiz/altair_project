from django.contrib.postgres import search
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from projects.choices import city_choices, scope_choices, state_choices, zone_choices

from .models import Project


def index(request):
    projects = Project.objects.order_by(
        '-create_date').filter(is_published=True)

    paginator = Paginator(projects, 3)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    context = {
        'projects': paged_projects
    }
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project
    }
    return render(request, 'projects/project.html', context)


def search(request):
    queryset_list = Project.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description_icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city_iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state_iexact=state)

    context = {
        'state_choices': state_choices,
        'projects': queryset_list,
        'values': request.GET
    }
    return render(request, 'projects/search.html', context)
