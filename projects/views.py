from django.contrib.postgres import search
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from projects.choices import city_choices, scope_choices, state_choices, zone_choices, goaltime_choices, budget_choices

from .models import Project, GanttImage


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
    ganttimage = GanttImage.objects.filter(project_id=project_id).latest('report_date')
    context = {
        'project': project,
        'ganttimage': ganttimage
    }
    return render(request, 'projects/project.html', context)


def search(request):
    queryset_list = Project.objects.order_by('-create_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Term of work, goal_time
    if 'goal_time' in request.GET:
        goal_time = request.GET['goal_time']
        if goal_time:
            queryset_list = queryset_list.filter(goal_time__lte=goal_time)

    # Budget allocated
    if 'budget_allocated' in request.GET:
        budget_allocated = request.GET['budget_allocated']
        if budget_allocated:
            queryset_list = queryset_list.filter(
                budget_allocated__lte=budget_allocated)

    # Scope of Project (i.e design, fuels, image)
    if 'scope' in request.GET:
        scope = request.GET['scope']
        if scope:
            queryset_list = queryset_list.filter(scope__iexact=scope)

    context = {
        'state_choices': state_choices,
        'budget_choices': budget_choices,
        'scope_choices': scope_choices,
        'goaltime_choices': goaltime_choices,
        'projects': queryset_list,
        'values': request.GET
    }
    return render(request, 'projects/search.html', context)

