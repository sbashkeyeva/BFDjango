from django.shortcuts import render
from .models import Restaurant
def home(request):
    rests=Restaurant.objects.all()
    context={
        'rests':rests
    }
    return render(request,'home.html',context)

