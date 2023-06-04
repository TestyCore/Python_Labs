# import requests
from django.shortcuts import render, redirect
from django.views import generic

import json
import base64
import uuid

from .models import OrderItem, Order
from cart.cart import Cart
from django.core.exceptions import PermissionDenied


def order_create(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("net dostpa")

    cart = Cart(request)
    if cart.get_total_price() == 0:
        return redirect('http://127.0.0.1:8000/edostavka/products/')
    if request.method == 'POST':
        order = Order.objects.create(client=request.user.username)

        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            item['product'].price += item['quantity']
            item['product'].save()

        cart.clear()
        # url = "https://api.yookassa.ru/v3/payments"  # Replace with the YooKassa API endpoint
        #
        # shop_id = "318870"  # Replace with your actual shopId
        # secret_key = "test_e6oCux8C5T90AegU9ba_zWHoW0BDVkiQowMv9xV4Ha0"  # Replace with your actual secret API key
        #
        # headers = {
        #     "Authorization": "Basic " + base64.b64encode(f"{shop_id}:{secret_key}".encode("utf-8")).decode("utf-8"),
        #     "Idempotence-Key": str(uuid.uuid4()),
        #     "Content-Type": "application/json"
        # }
        #
        # payload = {
        #     "amount": {
        #         "value": cart.get_total_price(),
        #         "currency": "RUB"
        #     },
        #     "capture": "true",
        #     "confirmation": {
        #         "type": "redirect",
        #         "return_url": "http://127.0.0.1:8000/edostavka/products/",
        #         "confirm_url": "https://localhost:7185/Cart/Index"  # Add the cancel URL here
        #     }
        # }
        #
        # response = requests.post(url, headers=headers, data=json.dumps(payload))
        # response_data = response.json()
        #
        # cart.clear()
        #
        # if response.ok:
        #     redirect_url = response_data["confirmation"]["confirmation_url"]
        #     return redirect(redirect_url)
        # else:
        #     # Handle the error response
        #     # You can access the error details from the response_data
        #     # and take appropriate action
        #     raise Exception("Failed to initiate payment. Error: " + response.text)
        # #
        # #
        # #
        return render(request, 'order/created.html',
                       {'order': order})

    return render(request, 'order/create.html',
                  {'cart': cart})


class OrderListView(generic.ListView):
    model = Order
