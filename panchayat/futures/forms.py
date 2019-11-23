from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class futures(forms.ModelForm):
    # cropName = forms.CharField(max_length=100)
    # cropVariety = forms.CharField(max_length=100)
    # Quantity= forms.IntegerField()
    # DeliveryDate=forms.DateField(widget=DateInput())
    # ProductionMode=forms.CharField(max_length=100)
    # ContractPrice=forms.IntegerField()
    # advance=forms.IntegerField()
    # AdvanceDate=forms.DateField(widget=DateInput())
    class Meta:
        model=FuturesContract
        fields = '__all__'
        widgets = {
            'DeliveryDate': DateInput(),
            'AdvanceDate':DateInput()
        }

