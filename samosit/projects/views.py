from django.shortcuts import render_to_response, get_object_or_404
from samosit.projects.models import Project
from django.template import RequestContext


def index(request):
    projects = Project.objects.all()
    return render_to_response('projects/project_index.html', {'projects' : projects}, context_instance=RequestContext(request))

def detail(request, project_id, slug):
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    return render_to_response('projects/project_detail.html', {'object' : project, 'projects': projects}, context_instance=RequestContext(request))