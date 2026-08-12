from django.shortcuts import render, get_object_or_404, redirect
from productApp.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .cart_service import add_to_db
from django.contrib.auth.decorators import login_required

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
    if request.user.is_authenticated:
        add_to_db(request, product_id)
    else:
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
        cart, _ = Cart.objects.get_or_create(user=request.user)                
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
    
    
def remove_item(request, product_id):
    
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        item =  get_object_or_404(CartItem, cart=cart, product_id = product_id)   
        if item.quantity == 1:
            item.delete()
        else:
            item.quantity -= 1
            item.save()
                          
    else:
        my_cart = request.session.get("cart", {})
        product_id = str(product_id)
        
        if my_cart.get(product_id):
            if my_cart.get(product_id) == 1:
                my_cart.pop(product_id) 
            else:
                my_cart[product_id] -= 1
      
            request.session["cart"] = my_cart
    
    return redirect('cart')


@login_required
def all_orders(request):
    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related('order_items__product')
        .order_by('-created_at')
    )
    return render(
        request,
        template_name="orderapp/all_orders.html",
        context={
            "orders": orders
        }
    )
    

@login_required 
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cart_items.all()
    if not cart_items:
        return redirect('cart')  # Redirect to cart if it's empty
    order = Order.objects.create(
        user=request.user,
        total_amount=sum(item.quantity * item.product.price for item in cart_items),
        payment_status='pending'
    )
    
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            item_price=item.product.price
        )
        
    # Clear the cart after checkout
    cart.cart_items.all().delete()
    
    return render(
        request,
        template_name="orderapp/checkout.html",
        context={
            "order": order
        }
    )