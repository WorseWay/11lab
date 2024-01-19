from django.db import models
from users.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    image = models.ImageField(upload_to='products_images')



    def __str__(self):
        return f'Мороженое:{self.name}'



class Basket(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} |Мороженое: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

