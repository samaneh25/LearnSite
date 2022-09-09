from django.db import models
from django.conf import settings


CHOICES = [
    ('۱ ماهه', '1m'),
    ('۳ ماهه', '2m'),
    ('۶ ماهه', '3m'),
]


class PlanModel(models.Model):
    period = models.CharField(max_length=6, choices=CHOICES)
    price = models.IntegerField(editable=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.period


class UserActivePLan(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(PlanModel, on_delete=models.CASCADE)
    is_plan_active = models.BooleanField()
    remain_date = models.IntegerField(editable=True, null=True)
