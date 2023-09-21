from django.db import models


# Create your models here.

class Produit(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="media")
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    about = models.TextField(max_length=255)
    slug = models.SlugField(default="abcd", blank=True, null=True)




def __str__(self):
    return self.name
