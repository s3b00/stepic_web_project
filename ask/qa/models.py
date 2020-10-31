from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')[:10]

    def popular(self):
        return self.all().order_by('-rating')[:10]


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.IntegerField(null=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-rating']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
