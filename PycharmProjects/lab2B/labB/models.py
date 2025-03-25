from django.db import models
from django.contrib.auth.admin import User


class Market(models.Model):
    name = models.CharField(max_length=100)
    num_markets = models.IntegerField()
    opening_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_from = models.TimeField()
    work_to = models.TimeField()

    def __str__(self):
        return f"{self.name}"


class Contact_Info(models.Model):
    ulica = models.CharField(max_length=100)
    broj = models.IntegerField()
    phone =  models.CharField(max_length=100)
    email = models.EmailField()
    market = models.OneToOneField(Market,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ulica} {self.broj}"



class Vraboten(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    embg = models.IntegerField()
    salary = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} "

class Product(models.Model):
    TYPE_CHOICES = [
        ('H', 'Hrana'),
        ('P', 'Pijalok'),
        ('P', 'Pekara'),
        ('K', 'Kozmetika'),
        ('Hi', 'Higiena')
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    code = models.CharField(max_length=100, unique=True)
    homeMade = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.type} {self.code}"


class Market_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} {self.market} {self.quantity}"
