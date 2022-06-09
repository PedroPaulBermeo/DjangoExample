import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

'''
#Revisar este es el modelo que no me permite crear una pregunta sin respuestas
class Question(models.Model):
    # id el campo ID no es necesario porque Django la crea por nosotros.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.choice_set.all().count() == 0:
            super().delete()
            raise Exception("Question must have at least one choice")
            '''
class Question(models.Model):
    #id Django lo genera automaticamente no hace falta crearlo, y lo hace incrementable y primary
    #question_text
    # pub_date
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")#Le coloco un nombre entendible

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #timedelta saca diferencia de tiempo, en este caso le digo que de un dia
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)#Le indico que el primer valor va a ser 0
    def __str__(self):
        return self.choice_text


