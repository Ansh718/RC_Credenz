# Generated by Django 4.0.5 on 2023-05-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_RC', '0022_alter_profile_lifeline3_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lifelin2_secondattempt',
            field=models.BooleanField(default=False),
        ),
    ]