from urllib.parse import quote

from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Order


def order_list_view(request):
    if not request.user.is_authenticated:
        target = quote(request.get_full_path())
        return redirect(f"{reverse('home')}?login=1&next={target}")
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_list.html", {"orders": orders})
