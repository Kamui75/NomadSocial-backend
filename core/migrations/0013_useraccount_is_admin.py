# Generated by Django 3.2.14 on 2022-08-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_useraccount_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]