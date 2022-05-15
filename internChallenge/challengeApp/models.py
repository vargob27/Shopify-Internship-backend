from django.db import models
from datetime import datetime

# Create your models here.
class WarehouseManager(models.Manager):
    def warehouseValidator(self, post_data):
        errors = {}
        if len(post_data['name']) < 2:
            errors['name'] = "Warehouse name must be at least 2 characters long!"
        if len(post_data['city']) < 2:
            errors['city'] = "City must be at least 2 characters long!"
        if len(post_data['state']) < 2:
            errors['state'] = "State must be at least 2 characters long!"
        elif len(post_data['country']) < 2:
            errors['country'] = "Country must be at least 2 characters long!"
        return errors

    def updateValidator(self, post_data):
        errors = {}
        if len(post_data['name']) == 0:
            errors['name'] = "Please enter a warehouse name!"
        if len(post_data['city']) == 0:
            errors['city'] = "Please enter a city!"
        if len(post_data['state']) == 0:
            errors['state'] = "Please enter a state!"
        elif len(post_data['country']) == 0:
            errors['country'] = "Please enter a country!"
        return errors

class InventoryManager(models.Manager):
    def inventoryValidator(self, post_data):
        errors = {}
        existingInventory = Inventory.objects.filter(productName = post_data['productName'])
        if len(post_data['productName']) < 2:
            errors['productName'] = "Product name must be at least 2 characters long"
        if len(post_data['description']) < 2:
            errors['description'] = "Product description must be at least 2 characters long"
        if len(post_data['price']) == 0:
            errors['price'] = "Please enter a price!"
        elif len(existingInventory) > 0:
            errors['duplicate'] = "Product with the same name already exists"
        return errors

    def updateValidator(self, post_data):
        errors = {}
        existingInventory = Inventory.objects.filter(productName = post_data['productName'])
        if len(post_data['productName']) == 0:
            errors['productName'] = "Please enter a product name!"
        if len(post_data['description']) == 0:
            errors['description'] = "Please enter a description!"
        if len(post_data['price']) == 0:
            errors['price'] = "Please enter a price!"
        return errors

class Warehouse(models.Model):
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    country = models.CharField(max_length=75)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = WarehouseManager()
    def __str__(self):
        return '%s' % (self.name)

class Inventory(models.Model):
    productName = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    location = models.ManyToManyField(Warehouse, related_name='inventory')
    objects = InventoryManager()
    def __str__(self):
        return '%s %s' % (self.productName, self.description)

