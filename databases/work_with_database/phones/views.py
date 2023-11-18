from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    match request.GET.get('sort'):
        case 'name':
            phones = phones.order_by('name')
        case 'max_price':
            phones = phones.order_by('price')
        case 'min_price':
            phones = phones.order_by('-price')
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)