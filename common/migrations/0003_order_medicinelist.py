# Generated by Django 2.2.5 on 2019-09-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20190919_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='medicinelist',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
