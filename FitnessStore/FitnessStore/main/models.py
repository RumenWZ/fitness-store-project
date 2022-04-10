from django.db import models

# Create your models here.
from FitnessStore.accounts.models import FitnessStoreUser
from FitnessStore.products.models import Protein


class Sales(models.Model):

    user = models.ForeignKey(
        FitnessStoreUser,
        on_delete=models.CASCADE,
    )

    # product = models.ForeignKey(
    #     Protein,
    #     on_delete=models.CASCADE,
    # )
    #
    # product_type = models.ForeignKey(
    #     Protein,
    #     on_delete=models.CASCADE,
    # )

    # purchase_date = models.DateField(
    #     auto_now_add=True,
    # )