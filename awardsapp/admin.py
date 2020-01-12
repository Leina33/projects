from django.contrib import admin

# Register your models here.
from .models import Location,tags, Projects,Image


class ProjectsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Projects)
admin.site.register(Image)
