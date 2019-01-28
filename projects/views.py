from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
