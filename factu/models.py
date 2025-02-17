from django.db import models
from factu_toro.models import BaseModel


# Create your models here.
class Lot(BaseModel):
    name_lot = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_lot


class Cattle(BaseModel):
    name_cattle = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_cattle
