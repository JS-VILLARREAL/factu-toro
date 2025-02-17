from django.db import models
from django.conf import settings
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    deteled_by_casecade = None

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="+",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="+",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True
