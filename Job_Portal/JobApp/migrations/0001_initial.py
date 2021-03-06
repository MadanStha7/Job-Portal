# Generated by Django 3.0.7 on 2020-09-08 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Airlines', 'Airlines'), ('Automotive Sales, Support & Service', 'Automotive Sales, Support & Service'), ('Banks', 'Banks'), ('Call Center', 'Call Center'), ('Consumer Products', 'Consumer Products'), ('Designing / Printing', 'Designing / Printing'), ('E-business', 'E-business'), ('Education', 'Education'), ('Event Management', 'Event Management'), ('Finance', 'Finance'), ('Governmental Company', 'Governmental Company'), ('Health', 'Health'), ('Hotels', 'Hotels'), ('Insurance', 'Insurance'), ('Information Technology', 'Information Technology'), ('Import/Export', 'Import/Export'), ('ISP', 'ISP'), ('Media', 'Media'), ('NGO', 'NGO'), ('Real Estate', 'Real Estate'), ('Travel Agency', 'Travel Agency')], max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('address', models.CharField(max_length=100, null=True)),
                ('contact', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('last_date', models.DateTimeField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobApp.Company')),
            ],
        ),
    ]
