from django.db import models

# Create your models here.


class Cat(models.Model):
    class Meta:
        db_table = 'cats'
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=20)
    birth_year = models.IntegerField(null=True)


def __str__(self):
    return self.name
