from django.db import models
from django.core.exceptions import ValidationError


def validate_reference(value):
    if len(value) != 8 and value.isalnum() is False:
        raise ValidationError(f"{value} should be 8 symbols long and should consists of letters and numbers only!")

# Create your models here.
class Candidate(models.Model):
    name = models.CharField()
    candidate_reference = models.CharField(validators=[validate_reference])
