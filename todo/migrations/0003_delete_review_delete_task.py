# Generated by Django 5.0.7 on 2024-07-17 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]