from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField("name", max_length=500)
    detail = models.TextField("detail")
    price = models.DecimalField("price", max_digits=5, decimal_places=2)
    affiliate_url = models.URLField("affiliate url", max_length=200)
    image_url = models.URLField("image url", max_length=200)
    tags = models.ManyToManyField("Tag", verbose_name=("tags"))
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    name = models.CharField(name="name", max_length=50)

    def __str__(self):
        return self.name
