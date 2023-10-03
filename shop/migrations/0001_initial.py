# Generated by Django 4.2.5 on 2023-09-28 23:54

from django.db import migrations, models
import django.db.models.deletion
import shop.custom_field
import shop.helpers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_homepage', shop.custom_field.CustomBooleanField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='PlantingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
                ('special', shop.custom_field.CustomBooleanField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('price_sale', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('price_real', models.DecimalField(decimal_places=0, max_digits=10)),
                ('total_sold', models.IntegerField(default=0)),
                ('summary', models.TextField()),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to=shop.helpers.get_file_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('planting_methods', models.ManyToManyField(to='shop.plantingmethod')),
            ],
            options={
                'verbose_name_plural': 'Article',
            },
        ),
    ]
