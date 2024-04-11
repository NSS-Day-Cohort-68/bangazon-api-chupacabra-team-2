from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from django.contrib.auth.models import User


class Store(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    name = models.CharField(
        max_length=50,
    )
    description = models.CharField(max_length=255)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product_count = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
