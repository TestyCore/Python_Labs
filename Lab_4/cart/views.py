from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from edostavka.models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    if not request.user.is_authenticated:
        return redirect('index')
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
