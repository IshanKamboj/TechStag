# Generated by Django 3.0.7 on 2020-08-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Post', '0003_auto_20200815_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='Coding', max_length=500),
        ),
    ]