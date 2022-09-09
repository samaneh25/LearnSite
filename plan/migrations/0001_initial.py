# Generated by Django 4.0 on 2022-09-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('۱ ماهه', '1m'), ('۳ ماهه', '2m'), ('۶ ماهه', '3m')], max_length=6)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]