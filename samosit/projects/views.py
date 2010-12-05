from django.shortcuts import render_to_response, get_object_or_404
from samosit.projects.models import Project
from django.template import RequestContext


def index(request):
    objects = Project.objects.all()
    imageurl = "/media/"+project.image
    return render_to_response('projects/project_index.html', {'objects' : objects, 'imageurl' : imageurl}, context_instance=RequestContext(request))

def detail(request, project_id, slug):
    project = get_object_or_404(Project, pk=project_id)
    imageurl = "/media/"+project.image.url
    return render_to_response('projects/project_detail.html', {'object' : project, 'imageurl' : imageurl}, context_instance=RequestContext(request))