import json

from django.shortcuts import render
from django.views import View
from .models import Product, Blog, Team, Order, OrderItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(View):
    def get(self, request):

        products = Product.objects.all()

        return render(request, "index.html", {"products": products})


class ShopView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        name = ""

        name = request.GET.get("product_name")

        if not name:
            products = Product.objects.all()
            return render(request, "shop.html", {"products": products})

        else:
            products = Product.objects.filter(name__icontains=name)
            return render(request, "shop.html", {"products": products})


class AboutUsView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        teams = Team.objects.all()
        return render(request, "about.html", {"teams": teams})


class ServiceView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        products = Product.objects.all()
        return render(request, "services.html", {"products": products})


class BlogView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, "blog.html", {"blogs": blogs})


class ContactView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        return render(request, "contact.html", {})


class CartView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        return render(request, "cart.html", {})


class CheckoutView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        return render(request, "checkout.html", {})


class ThankYouView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        return render(request, "thankyou.html", {})






