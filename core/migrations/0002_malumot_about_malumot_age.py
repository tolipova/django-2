# Generated by Django 4.2.6 on 2023-10-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='malumot',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='malumot',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
