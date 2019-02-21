from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Topic of a forum"""

    subject = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject + " " + self.text[:20]


class Comment(models.Model):
    """Comments on topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        return self.text