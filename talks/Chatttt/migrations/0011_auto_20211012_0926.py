# Generated by Django 3.2.8 on 2021-10-12 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatttt', '0010_auto_20211012_0922'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BasicDetail',
        ),
        migrations.AlterField(
            model_name='friends',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
