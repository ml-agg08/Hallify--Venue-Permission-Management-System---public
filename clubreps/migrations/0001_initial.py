# Generated by Django 5.1.6 on 2025-02-26 07:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubReps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('ER', 'Electrical and Computer Science Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), ('AR', 'B.ARCH')], default='CSE', max_length=3)),
                ('batch', models.CharField(max_length=5)),
                ('year', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3)),
                ('admno', models.IntegerField()),
                ('club', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clubrep_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
