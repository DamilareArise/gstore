from django.urls import path
from . import views as vw

urlpatterns = [
    path("", vw.productView, name="products"),
    path("product-detail/<int:product_id>/", vw.productDetail, name="product-detail"),
    path('add-product/', vw.addProduct, name="add-product"),
    path('add-brand/', vw.addBrand, name="add-brand"),
    path('add-category/', vw.addCategory, name="add-category"),
    path('add-image/<int:product_id>/', vw.addProductImage, name="add-image"),
    path('add-specification/<int:product_id>/', vw.addProductSpecification, name="add-specification"),
]