from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from .forms import RestaurantForm


def home(request):
    return render(request, 'home.html')


def rests(request):
    rests = Restaurant.objects.all()
    context = {'rests': rests}
    return render(request, 'rests.html', context)


def detailed_rest(request, id):
    rest = Restaurant.objects.get(pk=id)
    context = {'rest': rest}
    return render(request, 'detailed_rest.html', context)


def add_rest(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rests')
    else:
        form = RestaurantForm
    context = {'form': form}

    return render(request, 'add_rest.html', context)


def delete_rest(request, id):
    rest = Restaurant.objects.get(pk=id)
    rest.delete()
    return redirect('rests')


def delete_all_rest(request):
    rests = Restaurant.objects.all()
    rests.delete()
    return redirect('rests')


def update_rest(request, id):
    updated_rest = get_object_or_404(Restaurant, pk=id)
    form = RestaurantForm(request.POST or None, instance=updated_rest)
    if form.is_valid():
        form.save()
        return redirect('rests')
    return render(request, 'add_rest.html', {'form': form})
