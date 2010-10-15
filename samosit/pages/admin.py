from samosit.pages.models import Page
from django.contrib import admin


class PageAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'parent', 'metatitle', 'metadescription', 'metakeywords')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    
    
admin.site.register(Page, PageAdmin)