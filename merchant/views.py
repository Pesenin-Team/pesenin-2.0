from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Merchant
from .models import Makanan

# Create your views here.


def merchant(request):
    list_merchant = Merchant.objects.all()
    content = {
        "penjual": list_merchant
    }
    return render(request, 'merchant/index.html', content)


def makanan(request):
    # merchant = Merchant.objects.get(pk=pk)
    list_makanan = Makanan.objects.all()
    content = {
        "food": list_makanan
    }
    return render(request, 'makanan/index.html', content)


def detail_makanan(request, pk):
    food_details = Makanan.objects.get(pk=pk)
    content = {
        "food_detail": food_details
    }
    return render(request, 'makanan/display.html', content)

def search_merchant(request):
    nama = request.POST.get('search')
    try:
        merchant = Merchant.objects.get(nama_merchant = nama)
        return render(request, 'search_merchant.html', {'merchants': merchant})
    except Merchant.DoesNotExist:
        error = "Sorry looks like your food is not here."
        return render(request, 'search_merchant.html', {'error': error})

def search_makanan(request):
    nama = request.POST.get('search')
    try:
        makanan = Makanan.objects.get(nama = nama)
        return render(request, 'search_makanan.html', {'makanans': makanan})
    except Makanan.DoesNotExist:
        error = "Sorry looks like your food is not here."
        return render(request, 'search_makanan.html', {'error': error})

def display_merchant(request):
    if (request.method) == "GET":
        merchant_json = Merchant.objects.all().values('nama_merchant', 'desc', 'link_gambar')
        list_merchant = list(merchant_json)
        return JsonResponse(list_merchant, safe=False)

def display_makanan(request):
    if (request.method) == "GET":
        makanan_json = Makanan.objects.all().values('merchant', 'nama','deskripsi','foto')
        list_makanan = list(makanan_json)
        return JsonResponse(list_makanan, safe=False)
