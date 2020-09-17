# Generated by Django 3.0.7 on 2020-09-17 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0003_auto_20200913_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time'), ('freelance', 'freelance')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='skill_level',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('expert', 'expert')], default='beginner', max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='date_of_birth',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
