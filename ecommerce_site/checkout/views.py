from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MapP5GrmAGPMNVY6Cunz2ideE6YIEajHXr86kBrpyGzurq4A3OeF8c5XAUxO9OziTAvhFdPnXDkCU2T4cwNoRp500Tqj0spKz',
        'client_secret': 'sk_test_51MapP5GrmAGPMNVYUuUBJhHT67No2vcmkW0G3WM25zFMxDoHSfFAGunSxmCjTYMHyq3Z3ttfjhNUVy56zUXswkPS00GgShYaCR',
    }

    return render(request, template, context)