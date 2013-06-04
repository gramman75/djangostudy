from django.db import models
from taggit import managers

class Post(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    tags = managers.TaggableManager()
    
    def __unicode__(self):
        return self.subject