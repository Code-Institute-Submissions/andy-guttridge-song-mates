# Generated by Django 3.2.15 on 2022-10-07 08:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songmates_main', '0002_alter_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='genre2',
            field=models.CharField(blank=True, choices=[('POP', 'Pop'), ('ROC', 'Rock'), ('HIP', 'Hip Hop'), ('FUS', 'Fusion'), ('CLA', 'Classical')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='genre3',
            field=models.CharField(blank=True, choices=[('POP', 'Pop'), ('ROC', 'Rock'), ('HIP', 'Hip Hop'), ('FUS', 'Fusion'), ('CLA', 'Classical')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='genre4',
            field=models.CharField(blank=True, choices=[('POP', 'Pop'), ('ROC', 'Rock'), ('HIP', 'Hip Hop'), ('FUS', 'Fusion'), ('CLA', 'Classical')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='genre5',
            field=models.CharField(blank=True, choices=[('POP', 'Pop'), ('ROC', 'Rock'), ('HIP', 'Hip Hop'), ('FUS', 'Fusion'), ('CLA', 'Classical')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instru_skill2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instru_skill3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instru_skill4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instru_skill5',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]