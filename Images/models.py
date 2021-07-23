from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.tag


class Image(models.Model):

    image = models.ImageField(upload_to='images/', null=False)
    itag = models.ManyToManyField(Tag)
