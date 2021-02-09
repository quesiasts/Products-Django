from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=13, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=False)
