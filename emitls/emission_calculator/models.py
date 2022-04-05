from django.db import models

# Create your models here.
class Score(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    score = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # score = models.ForeignKey(Score, on_delete=models.CASCADE)