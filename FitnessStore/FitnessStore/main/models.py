from django.db import models

# Create your models here.
from FitnessStore.accounts.models import FitnessStoreUser
from FitnessStore.products.models import Protein, Clothing
import uuid

class Sales(models.Model):

    sale_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )

    buyer = models.ForeignKey(
        FitnessStoreUser,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Protein,
        on_delete=models.CASCADE,
    )