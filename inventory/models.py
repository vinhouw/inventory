from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100 ,null=True, blank=True)

    def __str__(self):
        return self.category_name


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    partNumber = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True)
    size = models.CharField(max_length=200,null=True, blank=True)
    received_quantity = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.FloatField(default=0,null=True, blank=True)
    description = models.CharField(max_length=220,null=True, blank=True)
    
    LOCATION_CHOICES = [
        ('TR','Trinity'),
        ('TPA', 'Tampa'),
        ('CLW', 'Clearwater'),
        ('BRK', 'Brooksville'),
    ]
    location = models.CharField(max_length=15, choices=LOCATION_CHOICES)
    # location = models.CharField(max_length=100)
    lastOrdered = models.DateTimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # patient is attached by user who create them
    url = models.URLField(blank=True)
    qrcode = models.ImageField(upload_to='qrcodes/',null=True, blank=True)


    def __str__(self):
        return self.name

    def get_total(self):
        """ total for one type of item in stock """
        total_qty = self.quantity + self.received_quantity
        return int(total_qty)
    
    def get_total_price(self):
        """ total cost of  item """
        total = self.get_total() * self.unit_price
        return int(total)

