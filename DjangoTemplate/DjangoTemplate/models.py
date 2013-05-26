'''
Created on 2013-5-26

@author: mike
'''

from django.db import models
from django.contrib import admin

#blog model
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BloqPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    search_fields = ('title',)

admin.site.register(BlogPost,BloqPostAdmin)