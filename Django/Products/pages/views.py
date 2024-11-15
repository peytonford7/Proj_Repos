from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})

def store_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order ={ 'get_cart_total': 0, 'get_cart_items': 0 }
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = { 'products': products, 'cartItems': cartItems, 'shipping': False }
    return render(request, "store.html", context)

def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order ={ 'get_cart_total': 0, 'get_cart_items': 0 }
        cartItems = order['get_cart_items']


    context = { 'items': items, 'order': order, 'cartItems': cartItems, 'shipping': False }
    return render(request, "checkout.html", context)

def cart_view(request):
    print("User is authenticated:", request.user.is_authenticated)
    print("Session data:", request.session.items())
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = { 'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False }
        cartItems = order['get_cart_items']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, "cart.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('ProductID:', productId)
    print('Action: ', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    print('Data: ', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
                country=data['shipping']['country'],
            )

    else:
        print('User is not logged in..')

    return JsonResponse('Payment Complete!', safe=False)