# Generated by Django 5.1.2 on 2024-10-28 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': ' Items'},
        ),
    ]
