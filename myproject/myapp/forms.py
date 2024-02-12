from django import forms
from .models import Commodity,Market,State

from django.contrib.auth.forms import AuthenticationForm



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Subscribers

# Register a User
class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'autofocus': True, 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Address', 'autofocus': True, 'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password', 'autofocus': True, 'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please Confirm Your Password', 'autofocus': True, 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __str__(self):
        return f'CreateUserForm for {self.Meta.model.__name__}'


# Login a User
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username', 'autofocus': True, 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password', 'autofocus': True, 'class': 'form-control'})
    )





# class CommudityForm(forms.ModelForm):
#     class Meta:
#         model = Commodity
#         fields ='__all__'
        
# class StateForm(forms.ModelForm):
#     class Meta:
#         model = State
#         fields ='__all__'
        
class MarketForm(forms.Form):
    commodity = forms.ModelChoiceField(queryset = Commodity.objects.all(),
    widget = forms.Select(attrs = {"hx-get":"load_state/","hx-target":"#id_state"})) 
    state = forms.ModelChoiceField(queryset=State.objects.none()),
    market = forms.ModelChoiceField(queryset=Market.objects.none()),
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['state'].queryset = State.objects.none()
        
        if "commodity" in self.data:
            commodity_id = int(self.data.get("commodity"))
            self.fields["state"].queryset = State.objects.filter(commodity_id = commodity_id)
            
            
        
            
 # Subscriber
class SubscribersForm(forms.ModelForm):
    class Meta:
        model=Subscribers
        widgets = {
            'email':forms.EmailInput(attrs={'placeholder':'Enter Your Email Address','autofocus':True,'class':'form-control'}),   
        }
        fields = ['email']