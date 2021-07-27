from django.db import models
from .validators import validate_8char_length, validate_alnum, validate_float_0_100


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    candidate_reference = models.CharField(max_length=8, validators=[validate_8char_length, validate_alnum])

class Score(models.Model):
    candidate = models.ForeignKey(Candidate, default=None, on_delete=models.CASCADE)
    score  = models.FloatField(validators=[validate_float_0_100])
