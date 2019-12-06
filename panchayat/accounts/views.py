from django.shortcuts import render
from django.shortcuts import render, redirect
from accounts.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import requests
import json


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

def user_login(request):
    
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        data={"username":username, "password":password }
        data=json.dumps(data)
        headers = {
                    
                "Content-Type": "application/json",
                "accept": "application/json",
            }
        
        API_ENDPOINT='http://127.0.0.1:3000/token-auth/'
            
        r = requests.post(url = API_ENDPOINT, data = data, headers=headers) 
        print("@@@@@@@@@@@",type(r))
        pastebin_url = r.content
        print("The pastebin URL is:%s"%pastebin_url)

        user=username

        arr=['1san', 'san', 'subu']

        t = user in arr
        
        if t:

            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponse("Your account was inactive.")
        
        
     
    else:
        return render(request, 'accounts/user_login.html', {})


def portfolio(request):
    return render(request,'accounts/portfolio.html')
    
