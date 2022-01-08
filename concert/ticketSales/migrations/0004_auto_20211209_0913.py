# Generated by Django 3.2.9 on 2021-12-09 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0003_auto_20211205_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concertmodel',
            options={'verbose_name': 'کنسرت', 'verbose_name_plural': 'کنسرت'},
        ),
        migrations.AlterModelOptions(
            name='locationmodel',
            options={'verbose_name': 'محل برگزاری', 'verbose_name_plural': 'محل برگزاری'},
        ),
        migrations.AlterModelOptions(
            name='profilemodel',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربر'},
        ),
        migrations.AlterModelOptions(
            name='ticketmodel',
            options={'verbose_name': 'بلیط', 'verbose_name_plural': 'بلیط'},
        ),
        migrations.AlterModelOptions(
            name='timemodel',
            options={'verbose_name': 'سانس', 'verbose_name_plural': 'سانس'},
        ),
        migrations.AlterField(
            model_name='concertmodel',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='نام کنسرت'),
        ),
        migrations.AlterField(
            model_name='concertmodel',
            name='Poster',
            field=models.ImageField(null=True, upload_to='concertImages/', verbose_name='پوستر'),
        ),
        migrations.AlterField(
            model_name='concertmodel',
            name='SingerName',
            field=models.CharField(max_length=100, verbose_name='خواننده'),
        ),
        migrations.AlterField(
            model_name='concertmodel',
            name='length',
            field=models.IntegerField(verbose_name='طول'),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='Address',
            field=models.CharField(default='تهران برج میلاد', max_length=500, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='IdNumber',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='شناسه'),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='Phone',
            field=models.CharField(max_length=11, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='capacity',
            field=models.IntegerField(verbose_name='ظرفیت'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Family',
            field=models.CharField(max_length=100, verbose_name='فامیلی'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Gender',
            field=models.IntegerField(choices=[('Man', 'مرد'), ('Woman', 'زن')], verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Profile',
            field=models.ImageField(upload_to='ProfileImages/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='Price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='ProfileModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.profilemodel', verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='ticketImage',
            field=models.ImageField(upload_to='TicketImages/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='timeModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.timemodel', verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='Seats',
            field=models.IntegerField(verbose_name='صندلی'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='StartDateTime',
            field=models.DateTimeField(verbose_name='زمان شروع'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='Status',
            field=models.IntegerField(choices=[('Start', 'فروش بلیط شروع شده است'), ('End', 'فروش بلیط تمام شده است'), ('Cancel', 'این سانس کنسل شده است'), ('Sales', 'در حال فروش  بلیط')], verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='concertModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.concertmodel', verbose_name='کنسرت'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='locationModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketSales.locationmodel', verbose_name='مکان'),
        ),
    ]