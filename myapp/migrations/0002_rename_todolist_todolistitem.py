# Generated by Django 4.2.9 on 2024-01-03 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='ToDoListItem',
        ),
    ]