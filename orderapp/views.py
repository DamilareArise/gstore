from django.shortcuts import render

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
    if my_cart.get(product_id):
        my_cart[product_id] += 1
    else:
        my_cart[product_id] = 1
        
    request.session["cart"] = my_cart
    
    return render(
        request,
        template_name="orderapp/cart.html",
        context={
            "cart": my_cart
        }
    )
    