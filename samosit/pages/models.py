from django.db import models
from django.conf import settings

import datetime

class Page(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=40)
    metatitle = models.CharField(max_length=69)
    metakeywords = models.CharField(max_length=150, blank=True, null=True)
    metadescription = models.CharField(max_length=156, blank=True, null=True)
    content = models.TextField()
    added = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)
    parent = models.ForeignKey('self', related_name='childs', null=True, blank=True)
    
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('page_detail', (), {
            'page_id': self.pk,
            'slug': self.slug})
        
