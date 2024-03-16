from django import forms
from core.models import CustomUser

class Register(forms.ModelForm):
    confirm_Password=forms.CharField(required=True,max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control","id":"form5Example1"}))
    class Meta:
        model=CustomUser
        fields=["username","phone_number","fullname","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "fullname":forms.TextInput(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }
    def save(self):
        clean_data=self.cleaned_data
        password=clean_data.pop("password")
        clean_data.pop("confirm_Password")
        user=CustomUser.objects.create(**clean_data)
        user.set_password(password)
        user.save()

class Login(forms.Form):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class Fopass(forms.Form):
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={"class":"form-control"}))

class Activate(forms.Form):
    token=forms.CharField( max_length=100, required=True)
    username=forms.CharField(max_length=50,required=True)
    
        

            



        

    
