from django.core.validators import MinValueValidator, MaxLengthValidator
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
    link = models.URLField()
    _score = models.FloatField(db_column='score', null=True)
    files = models.FileField(blank=True)

    def name(self):
        return self.firstname + ' ' + self.secondname

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        score_list = [i.score for i in self.comment_set.all()]
        score_before_round = (sum(score_list) / float(len(self.comment_set.all())))
        self._score = '%.2f' % round(score_before_round, 2)


    def __str__(self):
        return self.name()

class Comment(models.Model):
    """Comments on staff"""
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    _score = models.PositiveSmallIntegerField(db_column='score', validators=[MinValueValidator(1), MaxLengthValidator(6)])
    subject = models.CharField(null=True, max_length=50)
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        #self.staff.score = value

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text[:50] + '...'