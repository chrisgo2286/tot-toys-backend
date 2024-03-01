from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import CartItemSerializer
from .models import CartItem
from toy.models import Toy

class CartView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
        

@api_view(('GET',))
def cart_view(request):
    queryset = CartItem.objects.all()
    queryset = queryset.values('id', 'toy__id', 'toy__name', 'toy__price', 
        'toy__description', 'toy__photo', 'quantity')
    for item in queryset:
        item['total'] = item['toy__price'] * item['quantity']
    return(Response(queryset))

@api_view(('POST',))
def create_cart_item_view(request):
    userId = request.data['user']
    toyId = request.data['toy']
    toy = Toy.objects.filter(id=toyId)[0]
    user = User.objects.filter(id=userId)[0]
    
    userCart = CartItem.objects.filter(user=user)
    for item in userCart:
        if item.toy == toy:
            item.quantity += 1
            item.save()
            return(Response("Cart Updated!"))
    cartItem = CartItem(toy=toy, user=user)
    cartItem.save()

    return(Response(None))
