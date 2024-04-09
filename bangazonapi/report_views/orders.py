# views.py

from django.shortcuts import render
from bangazonapi.models import Order


# def paid_orders_report(request):
#     # Fetch orders that have been paid for
#     paid_orders = Order.objects.filter(payment__isnull=False)

#     # Add additional information (customer name, total paid, payment type) to each order
#     for order in paid_orders:
#         order.customer_name = order.customer.get_full_name()
#         order.total_paid = sum(item.product.price for item in order.lineitems.all())
#         order.payment_type = order.payment.type

#     Pass the paid orders data to the template
#     return render(request, "paid_orders_report.html", {"paid_orders": paid_orders})


# def paid_orders_report(request):
#     # Fetch all paid orders
#     paid_orders = Order.objects.filter(payment__isnull=False)

#     context = {"paid_orders": paid_orders}

#     return render(request, "paid_orders_report.html", context)


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
