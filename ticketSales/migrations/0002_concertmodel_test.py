# Generated by Django 3.2.9 on 2021-12-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertmodel',
            name='test',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
