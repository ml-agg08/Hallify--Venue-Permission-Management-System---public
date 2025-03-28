# Generated by Django 5.1.6 on 2025-03-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_usertype_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(choices=[('CR', 'Club Representative'), ('FC', 'Faculty Coordinator'), ('VFC', 'Venue Faculty Coordinator'), ('VFS', 'Venue Faculty Staff'), ('SCY', 'Security')], default='CR', max_length=3),
        ),
    ]
