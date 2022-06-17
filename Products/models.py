from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return f"Product {self.name} - description {self.description} - Price: {self.price}"

