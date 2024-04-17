# views.py

from django.shortcuts import render
from bangazonapi.models import Order


def paid_orders_report(request):
    paid_orders = Order.objects.filter(payment__isnull=False)

    orders_with_info = []

    for order in paid_orders:
        total_price = sum(item.product.price for item in order.lineitems.all())

        order_info = {
            "id": order.id,
            "customer_name": order.customer.user.first_name,
            "total_price": total_price,
            "payment_type": order.payment.merchant_name,
        }

        orders_with_info.append(order_info)

    return render(request, "paid_orders_report.html", {"paid_orders": orders_with_info})


def unpaid_orders_report(request):
    unpaid_orders = Order.objects.filter(payment__isnull=True)

    orders_without_payment = []

    for order in unpaid_orders:
        total_price = sum(item.product.price for item in order.lineitems.all())

        order_info = {
            "id": order.id,
            "customer_name": order.customer.user.first_name,
            "total_price": total_price,
        }

        orders_without_payment.append(order_info)

    return render(
        request, "unpaid_orders_report.html", {"unpaid_orders": orders_without_payment}
    )
