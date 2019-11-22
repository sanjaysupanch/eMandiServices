from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
import requests
# Create your views here.

def home(request):
    return render(request, 'futures_new_order.html')
def new_futures(request):
    if request.method=="POST":
        form=new_futures(request.POST)
        if form.is_valid():
            futures_item=form.save(commit=False)
            # host=form.cleaned_data.get("host")
            # host_instance= get_object_or_404(Host, name=host)
            # visitor_item.host=host_instance
            # visitor_item.save()
            print(futures_item.host.__dict__)
            context={
                'visitor':futures_item,
            }
            return render(request, 'visiting.html',context)
    else:
        form=Add_Visitor(request.POST or None, request.FILES or None)
    return render(request,'new_file.html',{'form':form})