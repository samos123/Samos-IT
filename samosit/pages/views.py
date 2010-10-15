from samosit.pages.models import Page
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse





    
    
def detail(request, page_id):
    p = get_object_or_404(Page, pk=page_id)
    return render_to_response('pages/page_detail.html', {
            'object': p,
        })