from django.db import models

class towork(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField()
    views = models.IntegerField(default=False)
    is_published = models.BooleanField(default=0)
    create_date = models.DateTimeField()
