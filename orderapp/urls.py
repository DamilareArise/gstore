from django.urls import path
from . import views as vw

urlpatterns = [
    path("add-to-cart/<int:product_id>/", vw.add_to_cart, name="add-to-cart"),
    path("remove-item/<int:product_id>/", vw.remove_item, name="remove-item"),
    path("cart/", vw.cartView, name="cart"),
    path("checkout/", vw.checkout, name="checkout"),
    path("orders/", vw.all_orders, name="all-orders")
]


