from django.db import models

# Create your models here.


#representing an individual task
class Task(models.Model):
    #Title of the task 
    title = models.CharField(max_length=200)
    
    #description of the task
    description = models.TextField(blank=True, null=True)
    
    #status indicator
    completed = models.BooleanField(default=False)
    
    #tracking when the task was initially created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title