# Generated by Django 2.2.24 on 2021-11-26 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211126_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='equipement',
            name='photo',
        ),
        migrations.AlterField(
            model_name='animal',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.equipement'),
        ),
    ]
