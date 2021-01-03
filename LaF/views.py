from django.shortcuts import render,redirect
from .models import Lost,Find
from .forms import Lost_Form,Find_Form
from .filters import LostFilter,FindFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.

def post(request):
    text="hjjjhjhjhj"
    return HttpResponse(text)

def home(request):
    return render(request, "home.html")

def master(request):
    return render(request, "master.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
'''
def lost_form(request):
    if request.method=='POST':
        form = Lost_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Lost_Form()
    return render(request, "lost form.html",{'form':form})
'''


def find_people(request):
    details_find_people = Find.objects.all()
    return render(request,'Find People.html',{'details_find_people':details_find_people})

def search_lost_people(request):
    user_list = Lost.objects.all()
    user_filter = LostFilter(request.GET, queryset=user_list)
    return render(request, 'search lost people.html', {'filter': user_filter})

def search_find_people(request):
    user_list = Find.objects.all()
    user_filter = FindFilter(request.GET, queryset=user_list)
    return render(request, 'search find people.html', {'filter': user_filter})

def lost_form(request):
    if request.method=='POST':
        form = Lost_Form(request.POST)
        mobile_no = request.POST.get('mobile_no')
        aadhaar_no=request.POST.get('aadhaar_no')
        PIN_code=request.POST.get('PIN_code')
        if (((len(mobile_no)) == 10)or((len(mobile_no)) == 0)):
            if (((len(aadhaar_no)) == 14)or((len(aadhaar_no)) == 0)):
                if(((len(PIN_code)) == 6)or((len(PIN_code)) == 0)):
                    if form.is_valid():
                        form.save()
                else:
                    messages.error(request, 'Your PIN code number is less then 6 digits')
            else:
                messages.error(request,'Your Aadhaar number is less then 14 digits')
        else:
            messages.error(request,'Your Mobile no is less then 10 digits')

    else:
        form = Lost_Form()
    return render(request, "lost form.html",{'form':form})


def find_form(request):
    if request.method=='POST':
        form = Find_Form(request.POST)
        mobile_no = request.POST.get('mobile_no')
        aadhaar_no = request.POST.get('aadhaar_no')
        PIN_code = request.POST.get('PIN_code')
        if ((len(mobile_no)) == 10) or ((len(mobile_no)) == 0):
            if ((len(aadhaar_no)) == 14) or ((len(aadhaar_no)) == 0):
                if ((len(PIN_code)) == 6) or ((len(PIN_code)) == 0):
                    if form.is_valid():
                        form.save()
                        return render(request, "home.html")
                else:
                    messages.error(request, 'Your PIN code number is less then 6 digits')
            else:
                messages.error(request, 'Your Aadhaar number is less then 14 digits')
        else:
            messages.error(request, 'Your Mobile no is less then 10 digits')
    else:
        form = Find_Form()
    return render(request, "Find form.html",{'form':form})

def lost_people(request):
    details_lost_people = Lost.objects.all()
    return render(request,'Lost People.html',{'details_lost_people':details_lost_people})
