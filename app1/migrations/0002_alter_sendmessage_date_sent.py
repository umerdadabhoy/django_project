# Generated by Django 5.0.6 on 2024-05-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmessage',
            name='date_sent',
            field=models.DecimalField(decimal_places=6, default=1715518335.476299, max_digits=100),
        ),
    ]
