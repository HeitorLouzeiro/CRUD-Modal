from django.db import models


# Create your models here.
class exampleModal(models.Model):
    name = models.CharField(max_length=100)
    fistName = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.fistName
