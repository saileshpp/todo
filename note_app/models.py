from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=25,blank=False)
    note = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title