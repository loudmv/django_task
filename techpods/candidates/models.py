from django.db import models
from .validators import validate_8char_length, validate_alnum, validate_float_0_100


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    candidate_reference = models.CharField(max_length=8, validators=[validate_8char_length, validate_alnum])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['candidate_reference'], name='unique_candidate'),
        ]

class Score(models.Model):
    candidate_reference = models.CharField(max_length=8, validators=[validate_8char_length, validate_alnum])
    score  = models.FloatField(validators=[validate_float_0_100])
