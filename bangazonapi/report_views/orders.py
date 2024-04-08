# views.py

from django.shortcuts import render
from bangazonapi.models import Order, OrderProduct


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


def paid_orders_report(request):
    # Fetch all paid orders
    paid_orders = Order.objects.filter(payment__isnull=False)
    # line_item = OrderProduct.objects.get()

    context = {"paid_orders": paid_orders}

    return render(request, "paid_orders_report.html", context)


# def paid_orders_report(request):
#     # Fetch all paid orders
#     paid_orders = Order.objects.filter(payment__isnull=False)

#     # Create a dictionary to store orders and their line items
#     orders_with_line_items = {}

#     # Loop through each paid order
#     for order in paid_orders:
#         # Fetch line items associated with the current order
#         line_items = OrderProduct.objects.filter(order=order)

#         # Store the order and its line items in the dictionary
#         orders_with_line_items[order] = line_items

#     context = {"orders_with_line_items": orders_with_line_items}

#     return render(request, "paid_orders_report.html", context)
