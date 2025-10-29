"""
URL configuration for DOMPizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# DOMPizza/urls.py
from django.contrib import admin
from django.urls import path
from pizza_menu import views  # use app views directly

urlpatterns = [
    path("admin/", admin.site.urls),

    # existing routes
    path("", views.menu, name="menu"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-confirmation/", views.order_confirmation_view, name="order_confirmation"),
    path("api/toppings/", views.get_toppings, name="get_toppings"),
    path("api/cart/add/", views.add_to_cart, name="add_to_cart"),

    # 🔥 Secret routes
    path("secret/", views.secret_menu, name="secret_menu"),
    # If you added the unlock-code option, keep this too; otherwise it's harmless
    path("secret/unlock/", views.secret_unlock, name="secret_unlock"),
]

]
