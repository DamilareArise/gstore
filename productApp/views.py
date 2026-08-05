from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImages, Brand
from .forms import ProductForm, BrandForm, CategoryForm, ProductImageForm, ProductSpecificationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

products = [
        {
            "id": 1,
            "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
            "price": 109.95,
            "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
            "category": "men's clothing",
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
            "rating": {
            "rate": 3.9,
            "count": 120
            }
        },
        {
            "id": 2,
            "title": "Mens Casual Premium Slim Fit T-Shirts ",
            "price": 22.3,
            "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
            "category": "men's clothing",
            "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
            "rating": {
            "rate": 4.1,
            "count": 259
            }
        },
        {
            "id": 3,
            "title": "Mens Cotton Jacket",
            "price": 55.99,
            "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
            "category": "men's clothing",
            "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
            "rating": {
            "rate": 4.7,
            "count": 500
            }
        },
        {
            "id": 4,
            "title": "Mens Casual Slim Fit",
            "price": 15.99,
            "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
            "category": "men's clothing",
            "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png",
            "rating": {
            "rate": 2.1,
            "count": 430
            }
        },
    ]
    
def user_is_staff(user):
    return user.is_authenticated and user.is_staff    
    

def homeView(request):
    # products = Product.objects.all().order_by("?")
    # products = Product.objects.filter(id = 1)
    # products = Product.objects.filter(price__lte = 500000, quantity__gte=5)
    # product = Product.objects.get(id = 1)
    # print(product.images.all())
    # images = ProductImages.objects.filter(product=product)
    # print(images)
    
    products = Product.objects.prefetch_related('images').prefetch_related('specifications').all().order_by("?")[:4]
    
    
    
    return render(
        request,
        template_name="index.html",
        context={
           "products":products
        }
    )
    

def productView(request):  
    products = Product.objects.prefetch_related('images').prefetch_related('specifications').all().order_by("-created_at")
    
    return render(
        request,
        template_name="products.html",
        context={
           'products': products
        }
    )
   
   
def productDetail(request, product_id):
    product = Product.objects.prefetch_related('images').prefetch_related('specifications').get(id = product_id)
    image_form = ProductImageForm()
    specification_form = ProductSpecificationForm()
    
    
    return render(
        request,
        template_name="product-detail.html",
        context={
            "product": product,
            "image_form": image_form,
            "specification_form": specification_form
        }
    )
    
    
    
# @login_required
@user_passes_test(user_is_staff)
def addProduct(request):
    if request.method == 'POST':
        # data = request.POST
        # title = data.get('title')
        # description = data.get('description')
        # price = data.get('price')
        # quantity = data.get('quantity')
        # brand_id = data.get('brand')
        
        
        # brand = get_object_or_404(Brand, id=brand_id)
        # Product.objects.create(
        #     title = title,
        #     price = price,
        #     quantity = quantity,
        #     description = description,
        #     brand = brand
        # )
        
        
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
        
            return redirect('product-detail', product_id=product.id)
        return redirect('add-product')
    
    else:
        form = ProductForm()
        brand_form = BrandForm()
        category_form = CategoryForm()
        return render(
            request,
            template_name="product-form.html",
            context={
                "form": form,
                "brand_form": brand_form,
                "category_form": category_form
            }   
        )
        
@user_passes_test(user_is_staff)
def addBrand(request):
    if request.method == 'POST':
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
        
    return redirect('add-product')

@user_passes_test(user_is_staff)
def addCategory(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
        
    return redirect('add-product')

@user_passes_test(user_is_staff)
def addProductImage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        image_form = ProductImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            
    return redirect('product-detail', product_id=product.id)


@user_passes_test(user_is_staff)
def addProductSpecification(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        specification_form = ProductSpecificationForm(request.POST)
        if specification_form.is_valid():
            specification = specification_form.save(commit=False)
            specification.product = product
            specification.save()
            
    return redirect('product-detail', product_id=product.id)
        