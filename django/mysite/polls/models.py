from django.db import models
from datetime import timedelta,datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    def __str__(self):
        return self.question_text
    def is_laster_info(self):
        return self.pub_date >= datetime.now()-timedelta(days=1)

class Choice(models.Model):
    vodes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
