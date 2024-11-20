from django import forms 


class GenerateQrCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=100, label='Restaurant Name')
    url = forms.URLField(max_length=200, label='Menu URL')  
