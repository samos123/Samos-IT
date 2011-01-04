from django.shortcuts import render_to_response
from django.template import RequestContext
from samosit.projects.models import Project

def index(request):
    projects = Project.objects.all()
    return render_to_response('home.html', {'projects' : projects}, context_instance=RequestContext(request))