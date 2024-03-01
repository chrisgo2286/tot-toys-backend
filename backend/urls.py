"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from toy.views import ToyView
from cart.views import cart_view, CartView, create_cart_item_view

router = routers.DefaultRouter()
router.register(r'toys', ToyView, 'toy')
router.register(r'cartItems', CartView, 'cartItem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tot-toys/', include(router.urls)),
    path('tot-toys/cart/', cart_view),
    path('tot-toys/cart/create/', create_cart_item_view)
]
