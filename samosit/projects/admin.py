from samosit.projects.models import Project
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'image', 'client', 'year', 'siteurl', 'content', 'metatitle', 'metadescription', 'metakeywords')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    
    
admin.site.register(Project, ProjectAdmin)