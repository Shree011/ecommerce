from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import *

def home(request):
    return render(request, 'accounts/dashboard.html')

def Product(request):
    #prd = 'shreyash'
    prd = product.objects.all()
    return render(request, 'accounts/products.html', {'ac' : prd})

def customer(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
