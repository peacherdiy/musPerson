from django.db import models
from django.db.models import permalink
from django.contrib import admin
from photo.fields.ThumbnailImageField import ThumbnailImageField

# Create your models here.
class Item(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=250)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__ (self) :
        return self.name
    
    @permalink
    def get_absolute_url(self):
        return ('item-detail' , None, {'object-id' : self.id})
    
class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField (max_length=100)
    image = ThumbnailImageField(upload_to='media/photos')
    caption = models.CharField(max_length=250, blank=True)
    
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
        
    @permalink
    def get_absolute_url(self):
        return ('photo-detail' , None, {'object-id' : self.id})
    
class PhotoInline(admin.StackedInline):
    model = Photo
    
class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    
admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
