# Generated by Django 5.1.6 on 2025-03-22 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('permissions', '0014_permission_fac_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='club.clubs'),
        ),
    ]
