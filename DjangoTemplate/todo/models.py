# coding:utf-8
from django.db import models

'''
任务状态  计划|已开始|已结束|
'''
from django.contrib import admin
class TaskStatus(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__ (self) :
        return self.name
   
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
'''
任务类型  社交|工作|生活|娱乐|
'''
class TaskType(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__ (self) :
        return self.name
    
'''
任务优先级  低|高|中|
'''
class TaskPriority(models.Model):
    name = models.CharField(max_length=250)
    
    def __unicode__ (self) :
        return self.name
    
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
# Create your models here.
class Task(models.Model):
    taskStatus = models.ForeignKey(TaskStatus)
    taskPriority = models.ForeignKey(TaskPriority)
    taskType = models.ForeignKey(TaskType)
    name = models.CharField (max_length=100)
    desc = models.TextField()
    timestamp = models.DateTimeField()
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'taskStatus', 'taskPriority', 'taskType')
    search_fields = ('name',)

admin.site.register(Task,TaskAdmin)
admin.site.register(TaskStatus,TaskStatusAdmin)
admin.site.register(TaskPriority,TaskPriorityAdmin)
admin.site.register(TaskType)