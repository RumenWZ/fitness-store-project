from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from FitnessStore.accounts.manager import FitnessStoreUserManager
from FitnessStore.common.validators import validate_only_letters


class FitnessStoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MIN_LEN = 5
    USERNAME_MAX_LEN = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_only_letters,
        )
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = FitnessStoreUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        FitnessStoreUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
