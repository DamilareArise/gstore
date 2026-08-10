from django.urls import path
from . import views as vw

urlpatterns = [
    path("add-to-cart/<int:product_id>/", vw.add_to_cart, name="add-to-cart"),
    path("cart/", vw.cartView, name="cart")
]


