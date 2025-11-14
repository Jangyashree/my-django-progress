from django.contrib import admin

# Register your models here.
from app.models import *

class CustomViewWebpage(admin.ModelAdmin):
    list_display=['pk','topic_name','name','url']
    list_display_links=['pk','name']
    list_editable=('url',)
    list_filter=['name']
    list_per_page=2
    search_fields=['name']

class CustomViewAccessrecord(admin.ModelAdmin):
    list_display=['name','author','date']
    list_editable=['date']

admin.site.site_header='Django AdminPage'
admin.site.site_title='Best'
admin.site.index_title='Super'

admin.site.register(Topic)
admin.site.register(Webpage,CustomViewWebpage)
admin.site.register(Accessrecord,CustomViewAccessrecord)

