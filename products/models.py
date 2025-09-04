from django.db import models


class Proudcut(models.Model):
    name = models.CharField(max_length=120, unique= True)
    description = models.TextField(blank= True)
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
    stock = models.PositiveIntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
