# Generated by Django 3.2.14 on 2022-08-02 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_useraccount_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
    ]