from django.shortcuts import render, redirect

from books.models import Book

def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'

    #       ЗНАЧНИЯ ИЗ БД
    books_bd = Book.objects.all()
    books = sorted([{
        "name": f"{b.name}",
        "author": f"{b.author}",
        "pub_date": f"{b.pub_date}",
        "slug": str(f"{b.slug}"),
    } for b in books_bd], key=lambda d: d['pub_date'])

    context = {
        "books": books,
        "pag": False,
    }
    return render(request, template, context)

def books_data(request, slug):
    template = 'books/books_list.html'

    books_bd = Book.objects.all()
    books = [{
        "name": f"{b.name}",
        "author": f"{b.author}",
        "pub_date": f"{b.pub_date}",
        "slug": "",
    } for b in books_bd if f"{b.pub_date}" == f"{slug}"]


    date_all = sorted([{
        "date": f"{b.pub_date}",
    } for b in books_bd
    ], key=lambda d: d['date'])
    date_all = [i for n, i in enumerate(date_all) if i not in date_all[n + 1:]]

    index_data = date_all.index({"date": slug})

    if index_data != 0:
        last_date = date_all[index_data - 1]
        back = "<"
    else:
        last_date = {"date": ""}
        back = ""

    if index_data != len(date_all) -1:
        next_date = date_all[index_data + 1]
        next_sim = ">"
    else:
        next_date = {"date": ""}
        next_sim = ""

    context = {
        "books": books,
        "pag": True,
        "last": last_date,
        "next": next_date,
        "back": back,
        "next_sim": next_sim,
    }

    return render(request, template, context)
