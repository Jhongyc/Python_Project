# Generated by Django 2.1.3 on 2019-02-18 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='code',
            field=models.CharField(default='sa', max_length=32),
            preserve_default=False,
        ),
    ]
