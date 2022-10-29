from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


PHONE = []
def show_catalog(request):
    template = 'catalog.html'

    #       ЗНАЧНИЯ ИЗ БД
    ph = Phone.objects.all()
    phone = [{
        "name": f"{p.name}",
        "price": f"{p.price}",
        "image": f"{p.image}",
        "release_date": f"{p.release_date}",
        "lte_exists": f"{p.lte_exists}",
        "slug": f"{p.slug}",
    } for p in ph]

    #       СОРТИРОВКА
    sort = request.GET.get("sort", None)

    if sort == "min_price":
        phone = sorted(phone, key=lambda d: d['price'])
    elif sort == "max_price":
        phone = sorted(phone, key=lambda d: d['price'], reverse = True)
    elif sort == "name":
        phone = sorted(phone, key=lambda d: d['name'])


    #       ПЕРЕДАЁМ В HTML
    context = {
        "phones": phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    ph = Phone.objects.all()

    for p in ph:
        if p.slug == slug:
            phone = {
        "name": f"{p.name}",
        "price": f"{p.price}",
        "image": f"{p.image}",
        "release_date": f"{p.release_date}",
        "lte_exists": f"{p.lte_exists}",
        "slug": f"{p.slug}",
    }

    context = {
        "phone": phone
    }
    return render(request, template, context)
