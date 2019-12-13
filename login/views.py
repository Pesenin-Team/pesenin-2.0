from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import quotes

# Create your views here.


def home(request):
    '''Render Home Pesenin'''
    if(request.user.is_authenticated):
        context = {
            "nama": request.user.get_full_name().split(" ")[0],
        }
        return render(request, 'home/index.html', context)
    return render(request, 'home/index.html',)

def display_quotes(request):
    if (request.method) == "GET":
        quotes_json = quotes.objects.all().values('quotes')
        list_quotes = list(quotes_json)
        return JsonResponse(list_quotes, safe=False)

@login_required(login_url='login:login')
def profile(request):
    """Render profile page."""
    context = {
        "profile": {
            "Nama lengkap": request.user.get_full_name(),
            "Nama pengguna": request.user.username,
            "Alamat surel": request.user.email,
            # "Kode organisasi": request.user.profile.org_code,
            # "Peran pengguna": request.user.profile.role,
            "Nomor Pokok Mahasiswa": request.user.profile.npm,
            "Fakultas": request.user.profile.faculty,
            "Jurusan": request.user.profile.study_program,
            # "Program pendidikan": request.user.profile.educational_program
        }
    }
    return render(request, "home/profile.html", context)
