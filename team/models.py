from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.TextField(unique=False)
    position = models.TextField(unique=False)
    hometown = models.TextField(unique=False)
    school = models.TextField(unique=False)
    
    class Meta(object):
        verbose_name_plural = "Players"
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Course, self).save(*args, **kwargs)
