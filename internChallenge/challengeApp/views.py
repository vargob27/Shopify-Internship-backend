from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    inventory = Inventory.objects.all()
    warehouses = Warehouse.objects.all()
    context = {
        'inv' : inventory,
        'warehouses' : warehouses
    }
    return render(request, 'index.html', context)

def createProduct(request):
    errors = Inventory.objects.inventoryValidator(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    Inventory.objects.create(
        productName = request.POST['productName'],
        description = request.POST['description'],
        price = request.POST['price']
    )
    return redirect('/')

def createWarehouse(request):
    errors = Warehouse.objects.warehouseValidator(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    Warehouse.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        country = request.POST['country'],
    )
    return redirect('/')

def product(request, productId):
    context = {
        'product' : Inventory.objects.get(id=productId),
        'warehouse' : Warehouse.objects.all()
    }
    return render(request, 'product.html', context)

def warehouse(request, warehouseId):
    warehouse = Warehouse.objects.get(id=warehouseId)
    context = {
        'product' : Inventory.objects.all(),
        'warehouse' : warehouse,
        'inventory' : warehouse.inventory.all()
    }
    return render(request, 'warehouse.html', context)

def editProduct(request, productId):
    context = {
        'product' : Inventory.objects.get(id=productId),
        'warehouse' : Warehouse.objects.all()
    }
    return render(request, 'editProduct.html', context)

def editWarehouse(request, warehouseId):
    context = {
        'product' : Inventory.objects.all(),
        'warehouse' : Warehouse.objects.get(id=warehouseId)
    }
    return render(request, 'editWarehouse.html', context)

def updateProduct(request, productId):
    errors = Inventory.objects.updateValidator(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/inventory/{productId}/edit')
    toUpdate = Inventory.objects.get(id=productId)
    toUpdate.productName = request.POST['productName']
    toUpdate.description = request.POST['description']
    toUpdate.price = request.POST['price']
    toUpdate.save()
    return redirect('/')

def updateWarehouse(request, warehouseId):
    errors = Warehouse.objects.updateValidator(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/warehouse/{warehouseId}/edit')
    toUpdate = Warehouse.objects.get(id=warehouseId)
    toUpdate.name = request.POST['name']
    toUpdate.city = request.POST['city']
    toUpdate.state = request.POST['state']
    toUpdate.country = request.POST['country']
    toUpdate.save()
    return redirect('/')

def deleteProduct(request, productId):
    toDelete = Inventory.objects.get(id=productId)
    toDelete.delete()
    return redirect('/')

def deleteWarehouse(request, warehouseId):
    toDelete = Warehouse.objects.get(id=warehouseId)
    toDelete.delete()
    return redirect('/')

def assignWarehouse(request, productId):
    context = {
        'product' : Inventory.objects.get(id=productId),
        'warehouses' : Warehouse.objects.all()
    }
    return render(request, 'assignWarehouse.html', context)

def assignWarehouseSuccess(request, productId):
    productToAssign = Inventory.objects.get(id=productId)
    warehouseToAssign = Warehouse.objects.get(id=request.POST['id'])
    productToAssign.location.add(warehouseToAssign)
    return redirect('/')

def removeInventory(request, productId, warehouseId):
    productToRemove = Inventory.objects.get(id=productId)
    warehouseRemovingProduct = Warehouse.objects.get(id=warehouseId)
    productToRemove.location.remove(warehouseRemovingProduct)
    return redirect('/')