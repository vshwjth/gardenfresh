from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.TextField(max_length=50)
    CAT = (
        ('V', 'Vegetables'),
        ('F', 'Fruits'),
        ('K', 'Kitchen'),
    )
    price = models.FloatField()
    stock = models.IntegerField()
    itemImg = models.ImageField(upload_to='images/', null=True)
    itemCategory = models.CharField(max_length=1, choices=CAT, null=True)

    def __str__(self):
        return str(self.itemName)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    FirstName = models.TextField(max_length=50)
    LastName = models.TextField(max_length=50)
    def __str__(self):
        return self.FirstName



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    placed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return str(self.order)
    
    @property
    def get_total(self):
        total = (self.product.price * self.quantity)
        return total

class orderAddress(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True,  blank=True)
    phno = models.TextField(max_length=10)
    address = models.TextField()
    PIN = models.TextField()

    def __str__(self):
        return str(self.order)
    
    @property
    def get_address(self):
        return str(self.adress + ', TamilNadu' + ", India" + str(self.pin) + "PH NO:" + str(self.phno))

