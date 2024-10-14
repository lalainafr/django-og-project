from django.db import models

# Categoies 
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

    
# Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Product
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # one to many relation
    Description = models.TextField(max_length=250, default='', blank=True, null=True)
    Image = models.ImageField(upload_to='uploads/product/')    
    # image will vbe uploaded in 'media/uploads/product' - cf MEDIAFILE
         
    def __str__(self) -> str:
        return self.name

# Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False) 
    
    def __str__(self) -> str:
        return self.product