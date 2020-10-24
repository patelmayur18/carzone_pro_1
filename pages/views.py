from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def index(request):
    team = Team.objects.all()
    fetured_car = Car.objects.order_by('-created_date').filter(is_fetured=True)
    latest_car = Car.objects.order_by('-created_date')
    context = {
        'team':team,
        'fetured_car':fetured_car,
        'latest_car':latest_car,
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

    