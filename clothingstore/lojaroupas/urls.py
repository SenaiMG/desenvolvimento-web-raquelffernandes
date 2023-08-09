from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index.html"),
    path("shop/", views.shop, name="shop"),
    path("detail/", views.detail, name="detail"),
    path("contact/", views.contact, name="contact"),
    path("checkout/", views.checkout, name="checkout"),
    path("cart/", views.cart, name="cart")
]