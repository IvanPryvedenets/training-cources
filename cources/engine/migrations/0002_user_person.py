# Generated by Django 4.1.1 on 2023-03-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='person',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
