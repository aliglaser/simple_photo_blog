from django.contrib import admin
from . import models


# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')



admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)