from django.shortcuts import render_to_response
from samosit.projects.models import Project
from django.template import RequestContext


def index(request):
    objects = Project.objects.all()
    return render_to_response('projects/project_index.html', {'objects' : objects}, context_instance=RequestContext(request))
