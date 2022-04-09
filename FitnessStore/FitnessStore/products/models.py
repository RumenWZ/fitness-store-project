from django.db import models


class Protein(models.Model):
    PROTEIN_NAME_MAX_LENGTH = 40
    PROTEIN_PRICE_MAX_DIGITS = 10

    name = models.TextField(
        max_length=PROTEIN_NAME_MAX_LENGTH,
    )

    description = models.TextField(
        blank=True,
        null=False,
    )

    price = models.DecimalField(
        max_digits=PROTEIN_PRICE_MAX_DIGITS,
        decimal_places=2,
    )

    amount_sold = models.IntegerField(
        default=0,
    )
