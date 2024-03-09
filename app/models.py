from django.db import models

class MathQuestion(models.Model):
    x = models.IntegerField()
    sign = models.CharField(max_length=1)
    y = models.IntegerField()
    answer = models.IntegerField()