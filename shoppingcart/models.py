import django.utils.timezone

from django.db import models
from datetime import datetime

# Basic inheritance for duplicated fields (main_color, secondary_color, brand):

class Product(models.Model):
    main_color = models.CharField(max_length=15)
    secondary_color = models.CharField(max_length=15, null=True)
    brand = models.CharField(max_length=30)
    catalog_inclusion_date = models.DateTimeField(default=django.utils.timezone.now, null=True)
    image_url = models.URLField(max_length=200, unique=True)
    description = models.TextField()

    class Meta:
        abstract = True

    # Overwrite the save() method to set the catalog_inclusion_date to the current date and time:
    def save(self, *args, **kwargs):
        if self.catalog_inclusion_date is None:
            self.catalog_inclusion_date = django.utils.timezone.now

# And now, both models:

class TShirt(Product):
    id = models.AutoField(primary_key=True, unique=True)
    size = models.CharField(max_length=3, choices=[('XXS', 'XXS' ), ('XS', 'XS' ), ('S', 'S' ), ('M', 'M' ), ('L', 'L' ), ('XL', 'XL' ), ('XXL', 'XXL')])
    fabric = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('UNISEX', 'Unisex')])
    sleeves = models.BooleanField()


class Cap(Product):
    id = models.AutoField(primary_key=True, unique=True)
    logo_color = models.CharField(max_length=30)


class Cart(models.Model):
    from datetime import datetime
    id = models.AutoField(primary_key=True, unique=True)
    creation_date = models.DateField(default=django.utils.timezone.now)
    caps = models.ManyToManyField(Cap, related_name='caps_by_cart')
    tshirts = models.ManyToManyField(TShirt, related_name='tshirts_by_cart')
