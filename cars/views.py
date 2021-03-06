from django.shortcuts import render, get_object_or_404
from .models import Car
# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    data = {
        'cars':cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data={
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    # if 'min_price' in request.GET:
    #     min_price = request.GET['min_price']
    #     max_price = request.GET['max_price']
    #     if max_price:
    #         cars.filter(price_gte=min_price, price_lte = max_price )
    data = {
        'cars':cars,
    }
    return render(request, 'cars/search.html',data)
