from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Customers(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Customer_Name = models.TextField()
    Legal_or_Natural_Person = models.CharField(max_length=50, choices=[('юридична', 'юридична'), ('фізична', 'фізична')])
    Address = models.TextField()
    Phone = models.TextField()
    Contact_Person = models.TextField()
    Bank_Account = models.TextField()

    def str(self):
        return self.Customer_Name


class Products(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Product_Name = models.TextField()
    Price = models.FloatField()
    Quantity_In_Store = models.IntegerField()

    def str(self):
        return self.Product_Name


class Sales(models.Model):
    Sale_ID = models.AutoField(primary_key=True)
    Sale_Date = models.DateField()
    Customer_ID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Sold_Quantity = models.IntegerField()
    Discount = models.FloatField(validators=[MinValueValidator(3), MaxValueValidator(20)])
    Payment_Method = models.CharField(max_length=50, choices=[('готівковий', 'готівковий'), ('безготівковий', 'безготівковий')])
    Need_Delivery = models.BooleanField()
    Delivery_Cost = models.FloatField()

