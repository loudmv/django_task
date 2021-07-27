from django.core.exceptions import ValidationError


def validate_8char_length(value):
    if len(value) != 8:
        raise ValidationError(f"{value} should be 8 symbols long.")
    return True

def validate_alnum(value):
    if value.isalnum() is False:
        raise ValidationError(f"{value} should consists of letters and numbers only.")
    return True

def validate_float_0_100(value):
    if value < 0 or value > 100:
        raise ValidationError(f"{value} should be a float between 0 and 100.")
    return True
