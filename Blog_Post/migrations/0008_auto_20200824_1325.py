# Generated by Django 3.0.7 on 2020-08-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Post', '0007_auto_20200823_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(default='', max_length=7000),
        ),
    ]
