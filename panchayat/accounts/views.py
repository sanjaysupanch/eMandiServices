from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import requests


def index(request):
    return render(request,'accounts/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts/portfolio.html')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def portfolio(request):
    response=request.get("http://127.0.0.1:8000/order/marketorder/")
    mydata=response.json()
    return render(request, 'accounts/portfolio.html', {
        'CropName': mydata['CropName'],
        'CropVariety': mydata['CropVariety'],
        'Quantity': mydata['Quantity'],
        'BasePrice': mydata['BasePrice'],

        })
