# Generated by Django 4.2.2 on 2023-06-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.CharField(blank=True, max_length=100, verbose_name='Tag'),
        ),
    ]