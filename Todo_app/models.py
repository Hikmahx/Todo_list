from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length= 200)
    added_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Todoes"