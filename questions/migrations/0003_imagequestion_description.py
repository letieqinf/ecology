# Generated by Django 3.2.9 on 2021-11-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_imageanswer_imagequestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagequestion',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
