from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

class Choice(models.Model):
    vodes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)