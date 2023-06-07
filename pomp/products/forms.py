from django import forms 
from .models import Contact_us , Newsletter 


class Contact_us_forms(forms.ModelForm) : 

    class Meta : 

        model = Contact_us 
        fields = ("__all__") 





class Newsletter_form(forms.ModelForm) : 
    class Meta : 
        model = Newsletter 
        fields = ("__all__")




class Newsletter_form2(forms.Form):
    your_emailname = forms.CharField(label="email_account", max_length=100)


    