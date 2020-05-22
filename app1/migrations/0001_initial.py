# Generated by Django 3.0.2 on 2020-05-22 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('college', models.CharField(max_length=50)),
                ('std', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=50)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('speak', models.CharField(max_length=100)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('pname', models.CharField(max_length=50)),
                ('pduration', models.CharField(max_length=100)),
                ('pdesc', models.TextField()),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('profile', models.TextField()),
                ('mobile', models.CharField(max_length=100)),
                ('social', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]