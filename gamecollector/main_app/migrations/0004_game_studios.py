# Generated by Django 3.1.1 on 2020-09-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200917_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='studios',
            field=models.ManyToManyField(to='main_app.Studio'),
        ),
    ]
