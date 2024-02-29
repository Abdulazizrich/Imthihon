from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import *
from .forms import *

def bolim(request):
    context = {
        'bolimlar': Bolim.objects.all()
    }
    return render(request, 'bolim.html', context)


def barcha_kitoblar(request):
    context = {
        'kitob': Kitob.objects.order_by('nom'),
    }
    return render(request, 'kitoblar.html', context)


def yangi_kitoblar(request):
    context = {
        'kitob': Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, 'yangi.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('kitob')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


def kitob(request):
    if request.method == 'POST':
        data = KitobForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/kitob/')
    context = {
        'kitob': Kitob.objects.all(),
        'form': KitobForm()
    }
    return render(request, 'kitoblar.html', context)

def kitob_ochir(request, id):
    Kitob.objects.get(id=id).delete()
    return redirect("/bir/")

def bir(request,id):
    context = {
        'kitob': Kitob.objects.filter(id=id)
    }
    return render(request, 'ochir.html', context)