from django.db import models

# Create your models here.


#representing an individual task
class Task(models.Model):
    #task title
    title = models.CharField(max_length=200)
    
    #task decription
    description = models.TextField(blank=True, null=True)
    
    #status indicator
    completed = models.BooleanField(default=False)
    
    #tracking when the task wascreated
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title