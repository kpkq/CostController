from django.db import models

# Create your models here.
from authentication.models import CostControlUser


class Spendings(models.Model):
    user = models.OneToOneField(CostControlUser, on_delete=models.CASCADE, db_index=True)
    info = models.JSONField(default='')

    def __str__(self):
        return self.user.username