from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDos(models.Model):
    title = models.CharField(max_length=50, help_text='Enter todo title.')
    notes = models.TextField(blank=True, help_text='Enter your todo.')
    creation_time = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)

    #Relationship to the users
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title