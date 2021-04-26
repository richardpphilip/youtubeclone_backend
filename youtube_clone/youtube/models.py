from django.db import models

# Create your models here.
class PageFeatures(models.Model):
    video_id = models.CharField(max_length=50, default=None)
    comment = models.CharField(max_length=100, default=None)
    like = models.IntegerField(default=0, null=True)
