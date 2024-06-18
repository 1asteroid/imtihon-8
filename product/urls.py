from django.urls import path
from .views import (HomePageView, ShopView, AboutUsView, ServiceView, BlogView, ContactView, CheckoutView, CartView,
                    ThankYouView)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("shop/", ShopView.as_view(), name="shop"),
    path("about-us/", AboutUsView.as_view(), name="about"),
    path("service/", ServiceView.as_view(), name="service"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("check-out/", CheckoutView.as_view(), name="checkout"),
    path("cart/", CartView.as_view(), name="cart"),
    path("thank-you/", ThankYouView.as_view(), name="thank"),
]