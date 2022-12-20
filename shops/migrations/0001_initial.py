# Generated by Django 4.1.4 on 2022-12-12 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200, unique=True)),
                ('cat_desc', models.TextField(blank=True)),
                ('cat_slug', models.SlugField(max_length=250, unique=True)),
                ('cat_image', models.ImageField(blank=True, upload_to='category')),
                ('cat_is_active', models.BooleanField(default=True)),
                ('cat_created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('cat_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=200, unique=True)),
                ('pro_desc', models.TextField(blank=True)),
                ('pro_slug', models.SlugField(max_length=250, unique=True)),
                ('pro_image', models.ImageField(blank=True, upload_to='product')),
                ('pro_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pro_stock', models.IntegerField()),
                ('pro_is_available', models.BooleanField(default=True)),
                ('pro_is_active', models.BooleanField(default=True)),
                ('pro_created_date', models.DateField(auto_now_add=True)),
                ('pro_updated_date', models.DateField(auto_now=True)),
                ('pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('pro_name',),
            },
        ),
    ]