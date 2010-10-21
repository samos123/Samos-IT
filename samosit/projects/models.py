from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=40)
    client = models.CharField(max_length=60, blank=True, null=True)
    metatitle = models.CharField(max_length=69)
    metakeywords = models.CharField(max_length=150, blank=True, null=True)
    metadescription = models.CharField(max_length=156, blank=True, null=True)
    content = models.TextField()
    siteurl = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='upload/projects')
    added = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        absolute_url = '/'+settings.PROJECTS_ROOT+str(self.pk)+'/'+self.slug
        return absolute_url
