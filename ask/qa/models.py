from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at').[0:10]
    
    def popular(self):
        return self.order_by('rating').[0:10]

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User)
    objects = QuestionManager
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)

