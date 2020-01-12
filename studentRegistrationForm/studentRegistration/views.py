from django.shortcuts import render
from . import forms

# Create your views here.
def homePageView(request):

    form = forms.Registration()

    if request.method == "POST":
        form = forms.Registration(request.POST)

        #Print data into the console if it's Validate
        if form.is_valid():

            print("First Name:"+form.cleaned_data['name'])
            print("Middle Name: "+form.cleaned_data['middlename'])
            print("Last Name: "+form.cleaned_data['lastname'])
            print("Email: "+form.cleaned_data['email'])
            print("Address One: "+form.cleaned_data['addressOne'])
            print("Address Two: "+form.cleaned_data['addressTwo'])
            print("City "+form.cleaned_data['city'])
            print("Post code: "+form.cleaned_data['postcode'])

    return render(request,'studentRegistration/index.html', {'form':form})

    
