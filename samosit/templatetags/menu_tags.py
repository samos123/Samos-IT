from django.template import Library, Node
from samosit.pages.models import Page
from samosit.projects.models import Project
register = Library()

@register.inclusion_tag('topnav.html')
def show_topnav():
    about_page = Page.objects.get(pk=1)
    projects = Project.objects.all()
    return {"about_page": about_page, "projects": projects}