from django import forms
from .models import Lost,Find
from django.contrib.auth.models import User


class Lost_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name'}),required=True,max_length=50)
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':"Father's name"}),required=True,max_length=50)
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','id':'inputPassword6','placeholder':"Mother's name"}),required=True,max_length=50)
    age = forms.CharField(required=True,widget=(forms.Select(attrs={'class':'form-control form-control-sm'},choices=Lost.CHOICE)))
    mobile_no = forms.CharField(max_length=10, required=True,widget=(forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Phone no'})))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'State name'}),required=True,max_length=50)
    district = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'District name'}),required=True,max_length=50)
    city_or_village = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'City/Village/Local area name'}),required=True,max_length=100)
    PIN_code = forms.IntegerField(widget=(forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Address PIN code'})))
    aadhaar_no = forms.IntegerField(required=True,widget=(forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'aadhaar'})))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Write about lost people'}),required=True,max_length=500)

    class Meta:
        model=Lost
        fields = ['name','father_name','mother_name','age','mobile_no','state','district','city_or_village','PIN_code','aadhaar_no','description']

class Find_Form(forms.ModelForm):
    name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Name'}),max_length=50)
    father_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': '', 'placeholder': "Father's name"}), max_length=50)
    mother_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': '', 'placeholder': "Mother's name"}), max_length=50)
    age = forms.CharField(required=True,widget=(forms.Select(attrs={'class': ''},choices=Lost.CHOICE)))
    mobile_no = forms.CharField(required=False,max_length=10, widget=(forms.TextInput(attrs={'class': '', 'placeholder': 'Phone no'})))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder': 'State name'}), max_length=50)
    district = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder': 'District name'}), max_length=50)
    city_or_village = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder': 'City/Village/Local area name'}),max_length=100)
    PIN_code = forms.IntegerField(required=False,widget=(forms.TextInput(attrs={'class': '', 'placeholder': 'Address PIN code'})))
    aadhaar_no = forms.IntegerField(required=False, widget=(forms.TextInput(attrs={'class': '', 'placeholder': 'aadhaar'})))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': '', 'placeholder': 'Write about lost people'}),max_length=500)

    class Meta:
        model=Find
        fields = ['name','father_name','mother_name','age','mobile_no','state','district','city_or_village','PIN_code','aadhaar_no','description']
