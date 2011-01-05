from django.shortcuts import render_to_response
from django.template import RequestContext
from samosit.projects.models import Project
from articles.models import Article

def index(request):
    articles = Article.objects.all()
    projects = Project.objects.all()
    return render_to_response('home.html', {'projects' : projects, 'articles' : articles}, context_instance=RequestContext(request))