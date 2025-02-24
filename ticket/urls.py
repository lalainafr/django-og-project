from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ticket'),
    path('product-details/<str:pk>', views.product_details, name='product-details'),
    path('product-create/', views.create_product, name='create-product'),
]
