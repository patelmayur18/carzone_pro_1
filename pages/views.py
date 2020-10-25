from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def index(request):
    team = Team.objects.all()
    fetured_car = Car.objects.order_by('-created_date').filter(is_fetured=True)
    latest_car = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('modal','city','year','body_style')
    modal_search = Car.objects.values_list('modal',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    context = {
        'team':team,
        'fetured_car':fetured_car,
        'latest_car':latest_car,
        # 'search_fields':search_fields,
        'modal_search':modal_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,"pages/index.html",context)

def about(request):
    team = Team.objects.all()
    context = {
        'team':team,
    }
    return render(request,"pages/about.html",context)

def contact(request):
    return render(request,"pages/contact.html")

def services(request):
    return render(request,"pages/services.html")

    