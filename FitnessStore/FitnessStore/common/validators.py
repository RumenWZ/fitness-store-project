from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Must contain only letters')


def check_superuser(user):
    return user.is_superuser
