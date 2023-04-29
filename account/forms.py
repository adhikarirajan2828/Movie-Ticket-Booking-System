
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django import forms
from .models import MyUser
# from .forms import RegisterForm
User = get_user_model()

class RegisterForm(forms.ModelForm):

    # first_name = forms.CharField(max_length=50, label='First Name',  widget=forms.TextInput())
    # last_name = forms.CharField(max_length=50, label='Last Name',  widget=forms.TextInput())

    # email = forms.EmailField(max_length=100, label='Email',  widget=forms.TextInput())
    # password = forms.CharField(max_length=150, label='Password',  widget=forms.PasswordInput(render_value=True))
    # confirm_password = forms.CharField(max_length=150, label='Confirm Password',  widget=forms.PasswordInput(render_value=True))
    
    class Meta:
        model = MyUser
        fields=["first_name","last_name","email","password","confirm_password"]
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "password":forms.PasswordInput(attrs={'class':'form-control'},render_value=True),
            "confirm_password":forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
        }
        
    # def save(self, commit=True, instance=None):
    #     if instance is not None:
    #         self.instance = instance
    #     return super().save(commit)
    
  
    
    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
            
    def save(self, commit=True):
        
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        user.set_password(self.cleaned_data['password'])

        user.save()
        
        return user
     

    def clean(self):
        print(self.cleaned_data.get('password'))
        print(self.cleaned_data.get('confirm_password'))
        if self.cleaned_data.get('password') != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('Passwords do not match')
        elif len(self.cleaned_data['password']) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        elif not any(char.isdigit() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one number')
        elif not any(char.isupper() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one uppercase letter')
        elif not any(char.islower() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one lowercase letter')
        elif not any(char.isalpha() for char in self.cleaned_data['password']):
            raise forms.ValidationError('Password must contain at least one letter')
        elif self.cleaned_data['first_name'] in self.cleaned_data['password']:
            raise forms.ValidationError('Password cannot contain first name')
        elif self.cleaned_data['last_name'] in self.cleaned_data['password']:
            raise forms.ValidationError('Password cannot contain last name')
        
        return self.cleaned_data
    


    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Email already exists')
        return self.cleaned_data['email']

    
class LoginForm(forms.Form):

    email = forms.CharField(max_length=150, label='Email', widget=forms.TextInput())
    password = forms.CharField(max_length=150, label='Password',  widget=forms.PasswordInput())

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        

        user = authenticate(email=email, password=password)
        if not user :
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data
  

  
class OtpForm(forms.Form):
    otp = forms.CharField(label="otp", widget=forms.TextInput())

    def clean(self):
        otp = self.cleaned_data.get('otp')
        return self.cleaned_data