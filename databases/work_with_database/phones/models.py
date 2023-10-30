from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField()
    release_date = models.CharField(max_length=40)
    lte_exists = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50)
    pass
