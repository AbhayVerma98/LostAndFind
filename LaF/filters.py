
from django.contrib.auth.models import User
from LaF.models import Lost,Find
import django_filters
from django import forms

class LostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'name'}))
    father_name= django_filters.CharFilter(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Father name'}))
    mother_name= django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Mother name'}))

    mobile_no= django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Phone no'}))
    state= django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'State'}))
    district= django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'District'}))
    city_or_village= django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'City/Village'}))
    aadhaar_no= django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Aadhaar no'}))

    class Meta:
        model = Lost
        fields = ['name','father_name','mother_name','age','mobile_no','state','district','city_or_village','aadhaar_no']


class FindFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'name'}))
    father_name = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Father name'}))
    mother_name = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Mother name'}))

    mobile_no = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Phone no'}))
    state = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'State'}))
    district = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'District'}))
    city_or_village = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'City/Village'}))
    aadhaar_no = django_filters.CharFilter(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Aadhaar no'}))

    class Meta:
        model = Find
        fields = ['name','father_name','mother_name','age','mobile_no','state','district','city_or_village','aadhaar_no']
