from django.db import models
from django.urls import reverse


class Category(models.Model):
    cat_name = models.CharField(max_length=200, unique=True)
    cat_desc = models.TextField(blank=True)
    cat_slug = models.SlugField(max_length=250, unique=True)
    cat_image = models.ImageField(upload_to='category', blank=True)
    cat_is_active = models.BooleanField(default=True)
    cat_created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('cat_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shops:AllProductCat', args=[self.cat_slug])

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    pro_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=200, unique=True)
    pro_desc = models.TextField(blank=True)
    pro_slug = models.SlugField(max_length=250, unique=True)
    pro_image = models.ImageField(upload_to='product', blank=True)
    pro_price = models.DecimalField(max_digits=10, decimal_places=2)
    pro_stock = models.IntegerField()
    pro_is_available = models.BooleanField(default=True)
    pro_is_active = models.BooleanField(default=True)
    pro_created_date = models.DateField(auto_now_add=True)
    pro_updated_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('pro_name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.pro_name

    def get_url(self):
        return reverse('shops:ProductDetails', args=[self.pro_category.cat_slug, self.pro_slug])





