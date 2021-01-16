from django.db import models
from ShikkhaOnirbanApp.models import Category
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django.db.models import Count, Sum, Avg
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='shop_product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail =models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_element', kwargs={'slug': self.slug})

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return " "



class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='shop_product/')

    def __str(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url