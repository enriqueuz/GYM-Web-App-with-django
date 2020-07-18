from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Payment(models.Model):
    payment_type = models.CharField(max_length=50)
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)
    reference = models.IntegerField()
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_type
