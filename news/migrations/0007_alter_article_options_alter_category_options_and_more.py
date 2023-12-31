# Generated by Django 4.2.5 on 2023-09-22 11:06
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_article_special_alter_category_is_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='feed',
            options={'verbose_name_plural': 'Feed'},
        ),
        migrations.AlterField(
            model_name='category',
            name='layout',
            field=models.CharField(choices=[('list', 'List'), ('gird', 'Grid')], default='list', max_length=10),
        ),
    ]
