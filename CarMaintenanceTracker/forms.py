##imports
from django.forms import ModelForm, DateInput, Select
from .models import Service, Account



##creates Account Form based on Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'



#creates Service Form Based On Service Model
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'mm/dd/yyyy'

            }),
            'service': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px'
            })
        }