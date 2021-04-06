from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.FileField(upload_to='categories/%Y/%m/%d',blank=True)

    def get_absolute_url(self):
        return reverse('potato:product_list', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name




class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.FileField(upload_to='products/%Y/%m/%d', blank=True)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('potato:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)

    index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name='images', on_delete=models.CASCADE)
    images = models.FileField(upload_to='products/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


