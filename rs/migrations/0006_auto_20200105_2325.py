# Generated by Django 3.0.1 on 2020-01-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs', '0005_summary_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='Phone',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
