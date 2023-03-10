#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Car, DetailShop
from .forms import GassingForm

# Add the following import


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  detail_shops_car_doesnt_have = DetailShop.objects.exclude(id__in = car.detail_shops.all().values_list('id'))
  gassing_form = GassingForm()
  return render(request, 'cars/detail.html', {'car': car, 'gassing_form': gassing_form, 'detail_shops':detail_shops_car_doesnt_have})

def add_gassing(request, car_id):
  form = GassingForm(request.POST)
  
  if form.is_valid():
    
    new_gassing = form.save(commit=False)
    new_gassing.car_id = car_id
    new_gassing.save()
  return redirect('detail', car_id=car_id)



class CarCreate(CreateView):
  model = Car
  fields = ['name', 'model', 'description', 'year']
  success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['model', 'description', 'year']
   
  

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

class DetailShopList(ListView):
  model = DetailShop

class DetailShopDetail(DetailView):
  model = DetailShop

class DetailShopCreate(CreateView):
  model = DetailShop 
  fields = '_all_'

class DetailShopUpdate(UpdateView):
  model = DetailShop
  fields = ['name', 'location']

class DetailShopDelete(DeleteView):
  model = DetailShop 
  success_url = '/detail_shops/'


def assoc_detail_shop(request, car_id, detail_shop_id):
  Car.objects.get(id=car_id).detail_shops.add(detail_shop_id)
  return redirect('detail', car_id=car_id) 