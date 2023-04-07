from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import NewUserForm, OrderCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView



def index(request):
    posts = Products.objects.all()
    return render(request, 'main/index.html', {'posts': posts})

def not_found(request):
    return render(request, 'main/404.html')

def about(request):
    return render(request, 'main/about.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def contakt(request):
    return render(request, 'main/contacts.html')

def product_page(request):
    return render(request, 'main/product_page.html')

def register_request(request):
    # message = ''
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(user)
            messages.success(request, 'Ви успішно зареєструвалися!')
            return redirect('autoris')
        else:
            messages.error(request, 'Невдала реєстрація. Недійсна інформація.')
            # message = 'Невдала реєстрація. Недійсна інформація.'
    else:
        form = NewUserForm()
    return render(request=request, template_name='main/regist.html', context={'register_form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Ви ввійшли як {username}.')
                return redirect('home')
            else:
                messages.error(request, 'Невірний логін або пароль!')
    form = AuthenticationForm()
    return render(request=request, template_name='main/auto.html', context={'login_form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "Ви успішно вийшли.")
    return redirect('home')

def error_404(request, exception):
    return render(request, 'main/404.html')


def order_create(request):
    # cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # cart.clear()
            return render(request, 'main/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'main/create.html',
                  {'form': form})

def order_completed(request):
    return render(request, 'main/created.html')

class ProductDetailView(DetailView):
    model = Products
    template_name = 'main/product_page.html'
    context_object_name = 'product'
