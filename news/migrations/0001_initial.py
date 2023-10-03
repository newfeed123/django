# Generated by Django 4.2.5 on 2023-09-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_homepage', models.BooleanField(default=False)),
                ('layout', models.CharField(choices=[('list', 'List'), ('gird', 'Grid')], default='List', max_length=10)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
            ],
        ),
    ]