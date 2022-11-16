from django.db import models

# Create your models here.
class Settings(models.Model):
    key = models.CharField(max_length=65)
    value = models.CharField(max_length=550)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Settings'    


class 