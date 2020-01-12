from django import forms
from django.core import validators


class Registration(forms.Form):
    """docstring for ."""
    name = forms.CharField(label='First Name',widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    middlename = forms.CharField(label='Middle Name',widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'Middle Name'}))
    lastname = forms.CharField(label='Last Name', widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(label="Student Email", widget=forms
    .TextInput(attrs={'class':'form-control','placeholder':'Email' }))
    addressOne = forms.CharField(label='Street Address 1',widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}))
    addressTwo = forms.CharField(label='Street Address 2',widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}))
    city = forms.CharField(label="City",widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
    postcode = forms.CharField(label='Post Code',widget=forms
    .TextInput(attrs={'class':'form-control', 'placeholder':'Post code'}))
