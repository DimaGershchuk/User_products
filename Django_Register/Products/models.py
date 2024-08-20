from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
