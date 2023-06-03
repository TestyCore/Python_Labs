from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=50, help_text='Enter a product category (e.g. Beverages)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Manufacturer(models.Model):
    """Model representing an manufacturer."""
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the URL to access a particular manufacturer instance."""
        return reverse('manufacturer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, {self.headquarters}, {self.email}'


class Product(models.Model):
    """Model representing a product"""
    title = models.CharField(max_length=100)

    # ManyToManyField used because Manufacturer can product many products. Products can be made by many manufactures.
    manufacturer = models.ManyToManyField(Manufacturer, help_text='Select a manufacturer for this product')

    composition = models.TextField(max_length=1000, help_text='Enter a product composition')
    ean = models.CharField('EAN', max_length=13, unique=True,
                           help_text='13 Character <a href="https://www.eancode.nl/wat-is-een-ean-code/">EAN code</a>')

    # Foreign Key used because product can only have one category, but categories can have multiple products
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this product."""
        return reverse('product-detail', args=[str(self.id)])

