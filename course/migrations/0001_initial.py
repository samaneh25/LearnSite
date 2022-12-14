# Generated by Django 4.0 on 2022-09-06 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('is_single_headline', models.BooleanField()),
                ('video_link', models.CharField(max_length=400)),
                ('description', models.TextField(max_length=1000)),
                ('is_super_course', models.BooleanField()),
                ('teacher_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseHeadlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
            ],
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
