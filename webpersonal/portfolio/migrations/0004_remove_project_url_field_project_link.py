# Generated by Django 5.1.1 on 2024-10-16 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_options_project_url_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url_field',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
    ]
