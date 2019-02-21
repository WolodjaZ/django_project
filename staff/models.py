from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

academic_rank_choices = (
        ('pz', 'profesor zwyczajny'),
        ('pn', 'profesor nadzwyczajny'),
        ('doc', 'docent'),
        ('mgr', 'magister'),)

class Staff(models.Model):
    """Information about academic staff"""
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    academic_rank = models.CharField(choices=academic_rank_choices, null=True, max_length=3)
    link = models.URLField(null=True)
    score = models.FloatField(db_column='score', null=True, blank=True)
    files = models.FileField(blank=True)

    def name(self):
        return self.firstname + ' ' + self.secondname

    def update_score(self):
        list_ranks = [value.score for value in self.comment_set.all()]
        score =  sum(list_ranks)/ float(len(self.comment_set.all())) #TODO something wrong with comment_set.all(), rapair
        self.score = format(score, '.2f')

    def __str__(self):
        return self.name()

class Comment(models.Model):
    """Comments on staff"""
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    subject = models.CharField(null=True, max_length=50)
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text[:50] + '...'