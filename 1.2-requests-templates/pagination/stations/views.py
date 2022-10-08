from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))

CONTEXT = []
def bus_stations(request):

    if len(CONTEXT):
        pass
    else:
        with open('stations/settings/BUS_STATION.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                CONTEXT.append({"Name": row['Name'], "Street": row["Street"], "District": row["District"]})


    page_number = int(request.GET.get("page", 1))

    paginator = Paginator(CONTEXT, 10)
    pagi = paginator.get_page(page_number)


    context = {
        'bus_stations': pagi,
        'page': pagi,
    }
    return render(request, 'stations/index.html', context)
