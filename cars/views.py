from django.shortcuts import render,get_object_or_404
from .models import Car
from  django.core.paginator import EmptyPage,Paginator
# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars,2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    modal_search = Car.objects.values_list('modal',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    context = {
        'cars':paged_cars,
        'modal_search':modal_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'body_style_search':body_style_search,

    }
    return render(request,'cars/cars.html', context)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    context = {
        'single_car':single_car,
    }
    return render(request,'cars/car-details.html', context)    

def search(request):
    cars = Car.objects.order_by('-created_date')
    # if 'keyword' in request.GET:
    #     keyword = request.GET['keyword']
    #     if keyword:
    #         cars = cars.filter(discription__icontains=keyword)

    if 'modal' in request.GET:
        modal = request.GET['modal']
        if modal:
            cars = cars.filter(modal__icontains=modal)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            cars = cars.filter(city__iexact=location)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)  

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price,price__lte=max_price)      

    modal_search = Car.objects.values_list('modal',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()                                          
    context = {
        'cars':cars,
        'modal_search':modal_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'body_style_search':body_style_search,
    }
    return render(request,'cars/search.html',context)    