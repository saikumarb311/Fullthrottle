from django.db import models
import pytz
import datetime
# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=20,primary_key=True)
    real_name=models.CharField(max_length=50)
    time_zone = pytz.all_timezones
    tz_choice=tuple(zip(time_zone,time_zone))
    tz=models.CharField(max_length=150,choices=tz_choice)

    def __str__(self):
        return self.real_name
    @property
    def activitys(self):
        return self.activity_set.all()

class Activity(models.Model):

    user=models.ManyToManyField(User)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

