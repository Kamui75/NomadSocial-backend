# Generated by Django 3.2.14 on 2022-07-30 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220731_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
    ]
