from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    details = models.TextField() 
    photo_1_url = models.TextField()
    photo_2_url = models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    quantity = models.IntegerField()

class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems', related_query_name='cartItem')
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cartItems', related_query_name='cartItem')
    quantity = models.IntegerField()

class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title