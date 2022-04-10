from django.db import models
from cloudinary import models as cloudinary_models
import uuid

from django.urls import reverse


class Protein(models.Model):
    PROTEIN_NAME_MAX_LENGTH = 60
    PROTEIN_PRICE_MAX_DIGITS = 10

    FLAVOUR_MAX_LEN = 45
    FLAVOUR_MIN_LEN = 3

    product_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=PROTEIN_NAME_MAX_LENGTH,
    )

    picture = cloudinary_models.CloudinaryField('image')

    description = models.TextField(
        blank=True,
        null=False,
    )

    price = models.DecimalField(
        max_digits=PROTEIN_PRICE_MAX_DIGITS,
        decimal_places=2,
    )

    flavour = models.CharField(
        max_length=FLAVOUR_MAX_LEN,
        blank=True,
        null=True,
    )

    amount_sold = models.IntegerField(
        default=0,
    )

    out_of_stock = models.BooleanField(
        default=False,
    )
