# Generated by Django 3.0.1 on 2020-01-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs', '0009_auto_20200107_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='content',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='education',
            name='gpa',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
