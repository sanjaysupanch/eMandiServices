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
import json

f = open("token.txt", 'r')
tokendata = f.read()
f.close()

def home(request):
    # print(tokendata)
    return render(request, 'futures_new_order.html')


def new_market_order(request):
    if request.method == "POST":
        form = market(request.POST)
        if form.is_valid():
            visitor_item = form.save(commit=False)
            CropName = form.cleaned_data.get("CropName")
            CropVariety = form.cleaned_data.get("CropVariety")
            Quantity = form.cleaned_data.get("Quantity")
            ClosingDate = form.cleaned_data.get("ClosingDate")
            ProductionMode = form.cleaned_data.get("ProductionMode")
            BasePrice = form.cleaned_data.get("BasePrice")

        print(CropName, CropVariety, Quantity, str(
            ClosingDate), ProductionMode, BasePrice)
        # closing=str(ClosingDate)
        # print(type(closing))
        # print(closing)
        year = ClosingDate.strftime("%Y")
        print("year:", year)
        month = ClosingDate.strftime("%m")
        print("month:", month)
        day = ClosingDate.strftime("%d")
        print("day:", day)
        data = {
            # print(closing, type(closing))
            "CropName": CropName,
            "CropVariety": CropVariety,
            "Quantity": Quantity,
            "ProductionMode": ProductionMode,
            "BasePrice": BasePrice,
            "ClosingDate": str(ClosingDate)
        }

        print(data)
        data = json.dumps(data)
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
            'Authorization': 'JWT '+ tokendata,
            #   Authorization: `JWT ${localStorage.getItem('token')}`,
        }

        print('***', data)
        API_ENDPOINT = 'http://localhost:8000/order/marketorder/'
        r = requests.post(url=API_ENDPOINT, data=data, headers=headers)
        pastebin_url = r.content
        print("The pastebin URL is:%s" % pastebin_url)
        # return HttpResponse('<h1>hweuwe</h1>')
        return redirect('new_market1')

    else:
        form = market(request.POST or None, request.FILES or None)
    return render(request, 'future/new_order_market.html', {'form': form})


def portfolio_market(request):
    headers = {
        "Content-Type": "application/json",
                        "accept": "application/json",
        'Authorization': 'JWT '+ tokendata,
        #   Authorization: `JWT ${localStorage.getItem('token')}`,
    }
    API_ENDPOINT = 'http://localhost:8000/order/myorder/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    # print(r.json())
    appointments = r.json()

    API_ENDPOINT = 'http://localhost:8000/order/getbids/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    print('*')
    # print(r.json())
    bids = r.json()

    for data in appointments:
        order = data['id']
        bid1 = 0.0
        bid2 = 0.0
        bid3 = 0.0
        bidslist = [0.0, 0.0, 0.0]
        for bid in bids:
            if(bid['order'] == order):
                bidslist.append(bid['price'])
                print('%', bidslist)
        bidslist.sort(reverse=True)
        print('@', bidslist)

        data['bid1'] = bidslist[0]
        data['bid2'] = bidslist[1]
        data['bid3'] = bidslist[2]

    pastebin_url = r.content
    # print('****', appointments)
    print("The pastebin URL is:%s" % pastebin_url)

    API_ENDPOINT = 'http://localhost:8000/order/myorderexec/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    # print(r.json())
    executed = r.json()
    # print('@@', r.json())
    # for data in r.json():
    #     print(data['id'])
    #     API_ENDPOINT = 'http://localhost:8000/order/executedorder/'+str(data['id'])+'/'
    #     p = requests.get(url=API_ENDPOINT, headers=headers)
    #     print(p.content)
    # for order in r.content:
    #     print(order)
    # appointments=r.json()
    return render(request, 'future/portfolio_market.html', {'appointments': appointments, 'executed': executed})


def sell_market(request, order_id, bid):
    print(order_id)
    print(bid)
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        'Authorization': 'JWT '+tokendata,
        #   Authorization: `JWT ${localStorage.getItem('token')}`,
    }

    API_ENDPOINT = 'http://localhost:8000/order/marketorder/'+str(order_id)+'/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    data = r.json()[0]
    print('&&',data)
    data = json.dumps(data)
    print('###', data)

    API_ENDPOINT = 'http://localhost:8000/order/marketorder/'+str(order_id)+'/'+str(bid)+'/'
    r = requests.put(url=API_ENDPOINT, data=data, headers=headers)
    pastebin_url = r.content
    # print('****', appointments)
    print("The pastebin URL is:%s" % pastebin_url)

    return redirect('new_market1')




def new_futures(request):
    if request.method == "POST":
        form = futures(request.POST)
        if form.is_valid():
            visitor_item = form.save(commit=False)
            CropName = form.cleaned_data.get("Crop")
            CropVariety = form.cleaned_data.get("CropVariety")
            Quantity = form.cleaned_data.get("Quantity")
            DeliveryDate = form.cleaned_data.get("DeliveryDate")
            AdvanceDate = form.cleaned_data.get("AdvanceDate")
            ProductionMode = form.cleaned_data.get("ProductionMode")
            ContractPrice = form.cleaned_data.get("ContractPrice")
            advance = form.cleaned_data.get("advance")
            print(DeliveryDate)
            print(visitor_item.__dict__)
            data = {"Quantity": Quantity,
                    "DeliveryDate": str(DeliveryDate),
                    "ProductionMode": ProductionMode,
                    "ContractPrice": ContractPrice,
                    "advance": advance,
                    "AdvanceDate": str(AdvanceDate)

                    }
            data = json.dumps(data)
            headers = {
                "Content-Type": "application/json",
                "accept": "application/json",
                'Authorization': 'JWT '+ tokendata,
                #   Authorization: `JWT ${localStorage.getItem('token')}`,
            }
            print('66666666666666666666666666')
            print(data)
            API_ENDPOINT = 'http://localhost:8000/order/futurecontract/'+str(CropName)+'/'+str(CropVariety)+'/'
            r = requests.post(url=API_ENDPOINT, data=data, headers=headers)
            pastebin_url = r.content
            print("The pastebin URL is:%s" % pastebin_url)
            return redirect('portfolio_futures')
    else:
        form = futures(request.POST or None, request.FILES or None)
    return render(request, 'future/new_order_futures.html', {'form': form})


def portfolio_futures(request):
    headers = {
        "Content-Type": "application/json",
                        "accept": "application/json",
        'Authorization': 'JWT '+ tokendata,
        #   Authorization: `JWT ${localStorage.getItem('token')}`,
    }
    API_ENDPOINT = 'http://localhost:8000/order/myfutures/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    # print(r.json())
    appointments = r.json()

    pastebin_url = r.content
    # print('****', appointments)
    print("The pastebin URL is:%s" % pastebin_url)
    # print('**',appointments[0]['Crop'])
    # API_ENDPOINT='http://localhost:8000/order/myorderexec/'
    # r = requests.get(url = API_ENDPOINT, headers=headers)
    # print(r.json())
    # executed=r.json()
    API_ENDPOINT = 'http://localhost:8000/order/futureexec/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    # print(r.json())
    executed = r.json()
    # appointments=r.json()
    # return HttpResponse('<h1> H </h1>')
    return render(request, 'future/portfolio_futures.html', {'appointments': appointments, 'executeds': executed})
