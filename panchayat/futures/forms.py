from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
    
class market(forms.ModelForm):

    class Meta:
        model=MarketOrder
        fields='__all__'
        widgets={
            'ClosingDate':DateInput(),
        }

class futures(forms.ModelForm):

    class Meta:
        model=FuturesContract
        fields = '__all__'
        widgets = {
            'DeliveryDate': DateInput(),
            'AdvanceDate':DateInput()
        }

