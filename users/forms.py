from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, widget=forms.RadioSelect)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    profile_picture = forms.ImageField(required=False)
    email = forms.EmailField(required=True)
    address_line1 = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=50, required=True)
    state = forms.CharField(max_length=50, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'first_name', 
                 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'email': forms.EmailInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'city': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'state': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'pincode': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_picture'].required = False

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
