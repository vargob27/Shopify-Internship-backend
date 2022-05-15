from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createProduct', views.createProduct),
    path('createWarehouse', views.createWarehouse),
    path('inventory/<int:productId>', views.product),
    path('warehouse/<int:warehouseId>', views.warehouse),
    path('inventory/<int:productId>/edit', views.editProduct),
    path('warehouse/<int:warehouseId>/edit', views.editWarehouse),
    path('inventory/<int:productId>/update', views.updateProduct),
    path('warehouse/<int:warehouseId>/update', views.updateWarehouse),
    path('inventory/<int:productId>/delete', views.deleteProduct),
    path('warehouse/<int:warehouseId>/delete', views.deleteWarehouse),
    path('inventory/assign/<int:productId>', views.assignWarehouse),
    path('inventory/<int:productId>/assign', views.assignWarehouseSuccess),
    path('inventory/<int:productId>/<int:warehouseId>/remove', views.removeInventory)
]
