from django.db import models
from django.db.models.enums import Choices
from jalali_date import datetime2jalali,date2jalali

# Create your models here.

class concertModel(models.Model):
  class Meta:
    verbose_name='کنسرت'
    verbose_name_plural='کنسرت'

  Name=models.CharField(max_length=100,verbose_name='نام کنسرت')
  SingerName=models.CharField(max_length=100,verbose_name='خواننده')
  length=models.IntegerField(verbose_name='طول')
  Poster=models.ImageField(upload_to="concertImages/",null=True,verbose_name='پوستر')

  def __str__(self):
    return self.SingerName

class locationModel(models.Model):
  class Meta:
    verbose_name='محل برگزاری'
    verbose_name_plural='محل برگزاری'

  IdNumber = models.IntegerField(primary_key=True,verbose_name='شناسه')
  Name=models.CharField(max_length=100,verbose_name='نام')
  Address=models.CharField(max_length=500,default='تهران برج میلاد',verbose_name='آدرس')
  Phone=models.CharField(max_length=11,verbose_name='شماره تلفن')
  capacity=models.IntegerField(verbose_name='ظرفیت')

  def __str__(self):
    return self.Name

class timeModel(models.Model):
  class Meta:
    verbose_name='سانس'
    verbose_name_plural='سانس'
  concertModel = models.ForeignKey("concertModel",on_delete=models.PROTECT,verbose_name='کنسرت')
  locationModel = models.ForeignKey("locationModel",on_delete=models.PROTECT,verbose_name='مکان')
  StartDateTime = models.DateTimeField(verbose_name='زمان شروع')
  Seats = models.IntegerField(verbose_name='صندلی')

  Start = 1
  End = 2
  Cancel = 3
  Sales = 4
  status_choices = ((Start,"فروش بلیط شروع شده است"),(End,"فروش بلیط تمام شده است"),(Cancel,"این سانس کنسل شده است"),(Sales,"در حال فروش  بلیط"),)

  Status = models.IntegerField(choices=status_choices,verbose_name='وضعیت')

  def __str__(self):
    return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime,self.concertModel.Name,self.locationModel.Name)
  def get_jalali_date(self):
    return datetime2jalali(self.StartDateTime)
class ProfileModel(models.Model):
  class Meta:
    verbose_name='کاربر'
    verbose_name_plural='کاربر'

  Name= models.CharField(max_length=100,verbose_name='نام')
  Family= models.CharField(max_length=100,verbose_name='فامیلی')
  Profile=models.ImageField(upload_to="ProfileImages/",verbose_name='تصویر')

  Man = 1
  Woman = 2
  status_choices = (("Man","مرد"),("Woman","زن"))

  Gender= models.IntegerField(choices= status_choices,verbose_name='جنسیت')

  def __str__(self):
    return "FullName: {} {}".format(Name,Family)


class ticketModel(models.Model):
  class Meta:
    verbose_name="بلیط"
    verbose_name_plural="بلیط"
  ProfileModel= models.ForeignKey("ProfileModel",on_delete=models.PROTECT,verbose_name='کاربر')
  timeModel= models.ForeignKey("timeModel",on_delete=models.PROTECT,verbose_name='تاریخ')
  ticketImage= models.ImageField(upload_to="TicketImages/",verbose_name='تصویر')
  Name = models.CharField(max_length=100,verbose_name='نام')
  Price= models.IntegerField(verbose_name='قیمت')

  def __str__(self):
    return "TicketInfo: Profile: {}".format(timeModel.__str__())