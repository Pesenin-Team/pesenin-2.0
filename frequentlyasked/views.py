from django.shortcuts import render

# Create your views here.

def frequentlyasked(request):
    return render(request, 'frequentlyasked/index.html')

