# Generated by Django 5.1.6 on 2025-03-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0011_permission_event_description_permission_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='event_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
