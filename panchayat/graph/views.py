from django.shortcuts import render
import requests
import json
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

f = open("token.txt", 'r')
tokendata = f.read()
f.close()

def mystic(request):
    
    if request.method == "POST":
        CropName=request.POST.get('CropName')
        CropVariety=request.POST.get('CropVariety')
        headers = {
                "Content-Type": "application/json",
                "accept": "application/json",
                'Authorization': 'JWT '+ tokendata,
        }

        API_ENDPOINT = 'http://localhost:8000/crop/pricedata/'+str(CropName)+'/'+str(CropVariety)+'/'
        
        print("********=>", API_ENDPOINT)
        
        r = requests.get(url=API_ENDPOINT, headers=headers)

        data=  r.json()
        data_dict = {}
        time_dict = {}
        timestamp=[]
        time = []
        price=[]
        
        for dat in data:
            try:
                data_dict[dat['timestamp'][:10][-2:]] += [(dat['timestamp'][:13][-2:], float(dat['price']))]
            except:
                data_dict[dat['timestamp'][:10][-2:]] = [(dat['timestamp'][:13][-2:], float(dat['price']))]
        final_data_time = {}
        for key in data_dict.keys():
            tempdict = {}
            for i,j in data_dict[key]:
                try:
                    tempdict[i] += [j]
                except:
                    tempdict[i] = [j]
            for k in tempdict.keys():        
                tempdict[k] = sum(tempdict[k])/len(tempdict[k])
            final_data_time[key] = tempdict


        print(final_data_time)
        
        return render(request,'graph/index.html', {'data':data, 'timestamp': final_data_time, 'CropVariety':CropVariety, 'CropName':CropName })
    
    else:
        return render(request, 'graph/index.html', {})