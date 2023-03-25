# Generated by Django 4.1.1 on 2023-03-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_user_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('person', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('person', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=100)),
                ('course1', models.CharField(blank=True, max_length=100)),
                ('course2', models.CharField(blank=True, max_length=100)),
                ('sertificate', models.ImageField(upload_to='')),
                ('sertificate1', models.ImageField(blank=True, upload_to='')),
                ('sertificate2', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]