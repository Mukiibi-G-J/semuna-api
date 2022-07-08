from django.db import models
from authentication.models import NewUser
from helpers.utilis import generate_code

from products.models import Product
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    transition_id = models.CharField(max_length=255, unique=True, blank=True)
    product = models.ManyToManyField(Product)
    fullName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    paymentMethod = models.CharField(max_length=255)
    itemsPrice = models.IntegerField()
    taxPrice = models.IntegerField()
    totalPrice = models.IntegerField()
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now=True)
    deliveredAt = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.transition_id = ""
        self.transition_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
