from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from .models import Cap, TShirt, Cart, Product
from django.forms.models import model_to_dict


def all_catalog(request):
    caps_serialized = list(Cap.objects.values())
    tshirts_serialized = list(TShirt.objects.values())

    # Now, we order the products by catalog_inclusion_date:
    caps_serialized.sort(key=lambda x: x['catalog_inclusion_date'], reverse=False)
    tshirts_serialized.sort(key=lambda x: x['catalog_inclusion_date'], reverse=False)

    return JsonResponse({'caps': caps_serialized, 't-shirts': tshirts_serialized})


def get_product(is_cap, product_id, cart):
    if is_cap:
        if Cap.objects.filter(id=product_id):
            product = Cap.objects.get(id=product_id)
            cart.caps.add(product)
        else:
            return HttpResponse('Error, no se puede añadir esta gorra. No existe en la base de datos')

    else:
        if TShirt.objects.filter(id=product_id):
            product = TShirt.objects.get(id=product_id)
            cart.tshirts.add(product)
        else:
            return HttpResponse('Error, no se puede añadir esta camiseta. No existe en la base de datos')

    cart.save()
    return HttpResponse('Añadido el producto ' + product.description + ' al carrito de la compra')


def add_to_cart(request):
    if request.method == 'POST':
        # Check for today's cart:

        body = json.loads(request.body)

        if Cart.objects.filter(creation_date=datetime.now().date()):
            cart = Cart.objects.get(creation_date=datetime.now().date())
        else:
            # There is no cart today. Create a new one:
            cart = Cart().save()
            cart.creation_date = datetime.now().date()
            cart.save()
        if body['product_id'] and body['type']:
            product_id = body['product_id']
            type = body['type']

            # We get the product from the database:
            if type.upper() == 'CAP':
                return get_product(True, product_id, cart)
            elif type.upper() == 'T-SHIRT':
                return get_product(False, product_id, cart)
        else:
            return HttpResponse('Error: El ID del producto o el tipo son inválidos.')
    else:
        return HttpResponse('Error: No se han especificado parámetros (POST).')


# View for the cart:

def view_cart(request):
    if not Cart.objects.filter(creation_date=datetime.now().date()):
        return HttpResponse('Error: No cart today.')

    cart = Cart.objects.get(creation_date=datetime.now().date())

    # Get the products in the cart:
    caps = list(cart.caps.values())
    tshirts = list(cart.tshirts.values())

    if cart:
        return JsonResponse({'creation_date': cart.creation_date, 'caps': caps, 'tshirts': tshirts})


def buy_cart_items(request):
    # Get today's cart:

    if not Cart.objects.filter(creation_date=datetime.now().date()):
        return HttpResponse('There is no cart for today.')
    cart = Cart.objects.get(creation_date=datetime.now().date())

    # Get the products in the cart:

    caps = list(cart.caps.values())
    tshirts = list(cart.tshirts.values())

    # Initial HTML text for the email (kind of a template):
    final_text = '<html lang="en"><head><meta charset="UTF-8"><h3>Has comprado los siguientes productos :</h3><table style="background-color: lightgray; border: 1px solid black">'

    if caps:
        final_text += 'Gorras:<br/>'

    for cap in caps:
        product_text = '<tr style="width: 100px; height: 100px;"><td align="center"><strong>{brand}</strong><br/><br/>{description}</td><td align="center" style="width:100px;"><img style="width: 80%; height: 80%; " src="{img_url}" alt=""></td></tr>'

        final_text += product_text.format(brand=cap['brand'], description=cap['description'], img_url=cap['image_url'])

    if tshirts:
        final_text += "<br/><hr style='border-top: 3px solid black;'>Camisetas:</hr><br/>"

    for tshirt in tshirts:
        product_text = '<tr style="width: 100px; height: 100px;"><td align="center"><strong>{brand}</strong><br/><br/>{description}</td><td align="center" style="width:100px;"><img style="width: 80%; height: 80%; " src="{img_url}" alt=""></td></tr>'

        final_text += product_text.format(brand=tshirt['brand'], description=tshirt['description'],
                                          img_url=tshirt['image_url'])

    from django.core.mail import send_mail

    send_mail(
        'Your order',
        '',
        'iaticarrito@gmail.com',
        ['sergidominguezrivas@gmail.com'],
        fail_silently=False,
        html_message=final_text
    )

    return HttpResponse('Your order has been sent.')
