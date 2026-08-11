from .models import Cart, CartItem
from productApp.models import Product
from django.shortcuts import get_object_or_404



def add_to_db(request, product_id, qty=1):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id = product_id)
                    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={
            "quantity": qty
        }
    )
    
    if not created:
        cart_item.quantity += qty
        cart_item.save()
        
        
        
def count_item(request):
    session_cart = request.session.get("cart", {})
    total_count = 0
    
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        if session_cart:
            for prod_id, qty in session_cart.items():
                add_to_db(request, prod_id, qty)   
                del request.session["cart"]
        
        for item in cart.cart_items.all():
            total_count += item.quantity
            
            
    else:
        for _, qty in session_cart.items():
            total_count += qty
    
    return {
        "total_count":total_count
    }