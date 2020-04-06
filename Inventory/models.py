from django.db import models
class Transaction(models.Model):
    Date = models.DateField(auto_now_add=True)
    Product_name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=19,decimal_places=5)
    Sale_able = models.IntegerField()
    Bounce = models.IntegerField()
    Sold = models.IntegerField(null=True)
    Balance = models.DecimalField(max_digits=19,decimal_places=5,null=True)
    Total_Balance = models.DecimalField(max_digits=19,decimal_places=5,null=True)

class Date(models.Model):
    Root = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now_add=True)