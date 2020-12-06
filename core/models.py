from django.db import models
import datetime

level_ch = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
class Subscriber(models.Model):
    level = models.CharField(choices=level_ch,max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image')
    debt = models.IntegerField()
    date_joined = models.DateTimeField()#auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name +' '+self.last_name

    @property
    def total_months(self):
        end_date = datetime.datetime.now()
        start_date = self.date_joined
        num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        return num_months



class Payment(models.Model):
    subscriber = models.ForeignKey(Subscriber,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.subscriber.first_name+' '+self.subscriber.last_name


    
class Fee(models.Model):
    level = models.CharField(choices=level_ch,max_length=20)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Debt(models.Model):
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.date)
