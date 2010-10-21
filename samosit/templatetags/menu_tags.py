from django.template import Library, Node
from samosit.pages.models import Page
register = Library()

@register.inclusion_tag('topnav.html')
def show_topnav():
    about_page = Page.objects.get(pk=1)
    return {"about_page": about_page}