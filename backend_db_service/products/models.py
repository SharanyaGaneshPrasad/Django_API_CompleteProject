from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField()

    def __str__(self):
        return self.product_name