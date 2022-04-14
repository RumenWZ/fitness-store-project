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

    out_of_stock = models.BooleanField(
        default=False,
    )

    type = models.TextField(
        default="Protein",
    )


class Clothing(models.Model):
    CLOTHING_NAME_MAX_LENGTH = 60
    CLOTHING_PRICE_MAX_DIGITS = 10

    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'

    SIZES = [(x, x) for x in (S, M, L, XL)]

    product_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=CLOTHING_NAME_MAX_LENGTH,
    )

    picture = cloudinary_models.CloudinaryField('image')

    description = models.TextField(
        blank=True,
        null=False,
    )

    price = models.DecimalField(
        max_digits=CLOTHING_PRICE_MAX_DIGITS,
        decimal_places=2,
    )

    size = models.CharField(
        max_length=max(len(x) for x, _ in SIZES),
        choices=SIZES,
        null=False,
        blank=False,
        default=S,
    )

    out_of_stock = models.BooleanField(
        default=False,
    )

    type = models.TextField(
        default="Clothing",
    )