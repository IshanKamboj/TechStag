# Generated by Django 3.0.7 on 2020-08-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Post', '0009_auto_20200824_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='heading_image',
            field=models.ImageField(default='pic.jpg', upload_to='Ishan'),
        ),
    ]