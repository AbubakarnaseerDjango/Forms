from django.db import models

# Create your models here.


class Info(models.Model):
    F_name = models.CharField(max_length=15)
    L_name = models.CharField(max_length=15)
    Email = models.EmailField(max_length=30)

    def __str__(self) :
        return self.F_name

        