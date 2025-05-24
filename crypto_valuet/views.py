from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from . import models

def index(request):
    # crcoins = models.CryptoCoins.objects.all()
    return render(request, "crypto_valuet.html")


def index(request):
    complex = {
        "crcoins":models.Crypto_Coins.objects.all(),
        "physiccoins":models.Physic_coin.objects.all(),
        "currensycoin":models.Currensy_coin.objects.all()
    }
    return render(request, 'crypto_valuet.html', complex)


def classs(request):
    complex_2 = {
        "CR_2":models.CryptoCoins.objects.all(),
        "PH_2":models.PhysicCoins.objects.all(),
        "CU_3":models.CurrensyCoins.objects.all()
    }
    return render(request, 'classs.html', complex_2)
##############################################################################################################
def single_1(request, idd):
    com = models.CryptoCoins.objects.get(pk=idd)
    return render(request, 'single_1.html', {'com':com})
# ##############################################################################################################
def single_2(request, idd):
    PHCOIN = models.PhysicCoins.objects.get(pk=idd)
    return render(request, 'single_2.html', {'PHCOIN':PHCOIN})
# ############################################################################################################
def single_3(request, idd):
    CURCOIN = models.CurrensyCoins.objects.get(pk=idd)
    return render(request, 'single_3.html', {'CURCOIN':CURCOIN})

# crypto_valuet/views.py
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # o‘zingizga mos URL
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
