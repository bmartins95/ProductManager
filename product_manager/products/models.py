from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    newproduct = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("products:product-delete", kwargs={"id": self.id})
