from django.contrib.auth.forms import UserCreationForm
from django import forms
from road.models import User,RoadViolation

class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),label="Enter Password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}),label="Confirm Password")

    class Meta:

        model=User

        fields=["username","email","phone"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter E-Mail"}),
            "phone":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Phone Number"}),
        }


class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),label="Enter Username")
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),label="Enter Password")