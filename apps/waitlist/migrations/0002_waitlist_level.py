# Generated by Django 4.0.2 on 2022-02-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlist',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Class Level'),
        ),
    ]
