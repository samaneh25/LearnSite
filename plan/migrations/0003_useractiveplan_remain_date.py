# Generated by Django 4.0 on 2022-09-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_useractiveplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractiveplan',
            name='remain_date',
            field=models.IntegerField(null=True),
        ),
    ]