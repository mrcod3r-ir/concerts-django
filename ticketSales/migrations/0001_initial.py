# Generated by Django 3.2.9 on 2021-12-04 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='concertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('SingerName', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='locationModel',
            fields=[
                ('IdNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(default='تهران برج میلاد', max_length=500)),
                ('Phone', models.CharField(max_length=11)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='timeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDateTime', models.DateTimeField()),
                ('Seats', models.IntegerField()),
                ('Status', models.IntegerField(choices=[('Start', 'فروش بلیط شروع شده است'), ('End', 'فروش بلیط تمام شده است'), ('Cancel', 'این سانس کنسل شده است'), ('Sales', 'در حال فروش  بلیط')])),
                ('concertModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.concertmodel')),
                ('locationModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.locationmodel')),
            ],
        ),
    ]
