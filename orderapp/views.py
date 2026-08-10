from django.shortcuts import render, get_object_or_404, redirect
from productApp.models import Product
from .models import Cart, CartItem

# Create your views here.

def add_to_cart(request, product_id):
    # session ={
    #     "cart": {
    #         "product_id": "product quatity",
    #     },
    #     "user_preferences": {
    #         "currency": "USD",
    #         "language": "en",
    #     }
    # }
    
    
    my_cart = request.session.get("cart", {})
    product_id = str(product_id)
    if my_cart.get((product_id)):
        my_cart[product_id] += 1
    else:
        my_cart[product_id] = 1
        
    request.session["cart"] = my_cart
    
    return redirect('cart')
    
    
def cartView(request):
    cart_obj = []
    total = 0
    session_cart = request.session.get("cart", {})
    
    
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(id=request.user.id)
        if session_cart:
           for prod_id, qty in session_cart.items():
                prod_id = int(prod_id)
                product = get_object_or_404(Product, id = prod_id)
                
                cart_item, created = CartItem.objects.get_or_create(
                    cart=cart,
                    product=product,
                    defaults={
                        "quantity": 1
                    }
                )
                
                if not created:
                    cart_item.quantity += 1
                    cart_item.save()
            
        else:
            
            cart_items = cart.cart_items.all()
            
            for item in cart_items:
                product = item.product
                subtotal = item.quantity * product.price
                cart_obj.append({
                    "product": product,
                    "qty": item.quantity,
                    "subtotal": subtotal
                })
                total += subtotal
    
    else:    
        for prod_id, qty in session_cart.items():
            prod_id = int(prod_id)
            product = get_object_or_404(Product, id = prod_id)
            subtotal = qty * product.price
            cart_obj.append({
                "product": product,
                "qty": qty,
                "subtotal": subtotal
            })
            total += subtotal

    
    return render(
        request,
        template_name="orderapp/cart.html",
        context={
            "cart": cart_obj,
            "total": total
        }
    )
    