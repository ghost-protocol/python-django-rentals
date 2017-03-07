from django.shortcuts import render, get_object_or_404
from .models import Cartype, Car, Location, Client, Order
from django.utils import timezone
from django.shortcuts import redirect
from .forms import OrderForm

# Create your views here.
# def home(request):
# 	return render(request,"cars/home.html")

def home(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.created = timezone.now()
			order.modified = timezone.now()
			order.save()
	else:
		form = OrderForm()
	return render(request, 'cars/home.html', {'form': form})