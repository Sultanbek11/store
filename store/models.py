from django.db import models


class Store(models.Model):
    name_store = models.CharField(max_length=200)
    filial = models.CharField(max_length=200)
    name_director = models.CharField(max_length=100)

    def __str__(self):
        return self.name_store


class Product(models.Model):
    title = models.CharField(max_length=200)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    count = models.IntegerField()
    price = models.IntegerField()
    instock = models.BooleanField(default=False)

    def __str__(self):
        return self.title
