from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
    
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="brands")
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        ("IN_STOCK", 'In Stock'),
        ('OUT_OF_STOCK', 'Out Of Stock')
    ]
    
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="IN_STOCK")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product_images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    is_cover = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.image.name

    
class ProductSpecification(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title + "-" + self.key
