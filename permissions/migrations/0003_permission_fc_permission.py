# Generated by Django 5.1.6 on 2025-03-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0002_alter_permission_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='fc_permission',
            field=models.CharField(default='no'),
        ),
    ]
