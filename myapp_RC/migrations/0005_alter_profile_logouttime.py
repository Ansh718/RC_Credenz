# Generated by Django 4.1.1 on 2023-05-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_RC', '0004_profile_correctanswers_profile_logouttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='logoutTime',
            field=models.DateTimeField(null=True),
        ),
    ]
