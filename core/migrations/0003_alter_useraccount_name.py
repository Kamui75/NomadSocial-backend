# Generated by Django 3.2.14 on 2022-07-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_useraccount_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]