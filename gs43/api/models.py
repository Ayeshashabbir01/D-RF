

# Create your models here.
from django.db import models



# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    singer = models.ForeignKey(Singer, related_name='sungby', on_delete=models.CASCADE)

    def __str__(self):
        return self.title