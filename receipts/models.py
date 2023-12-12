from django.db import models

# Create your models here.

class Receipt(models.Model):
    store_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    item_list = models.CharField(max_length=200)
    total_amount = models.IntegerField()

    def __str__(self):
        return f'Receipt from {self.store_name}, total amount : {self.total_amount}'