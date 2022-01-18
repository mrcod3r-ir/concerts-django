# Generated by Django 3.2.9 on 2022-01-17 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketSales', '0006_alter_timemodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='ProfileModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profilemodel', verbose_name='کاربر'),
        ),
        migrations.DeleteModel(
            name='ProfileModel',
        ),
    ]