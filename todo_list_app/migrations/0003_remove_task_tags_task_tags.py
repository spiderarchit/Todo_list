# Generated by Django 4.2.2 on 2023-06-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0002_remove_task_tags_task_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, to='todo_list_app.tag'),
        ),
    ]
