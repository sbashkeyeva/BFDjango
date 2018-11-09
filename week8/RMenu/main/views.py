from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Dish
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import RestaurantForm, DishForm
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    TemplateView,
    DetailView
)


class HomeView(TemplateView):
    template_name = 'home.html'


class RestListView(ListView):
    model = Restaurant
    context_object_name = 'rests'
    template_name = 'rests.html'


class RestCreateView(CreateView):
    model = Restaurant
    fields = ['name', 'number', 'telephone', 'city']
    template_name = 'add_dish.html'
    success_url = reverse_lazy('rests')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RestDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('rests')


class RestUpdateView(UpdateView):
    model = Restaurant
    fields = ['name', 'number', 'telephone', 'city']
    template_name = 'add_dish.html'
    success_url = reverse_lazy('rests')


class RestDetailView(DetailView):
    model = Restaurant
    template_name = 'detailed_rest.html'
    context_object_name = 'rest'


def home(request):
    return render(request, 'home.html')


def rests(request):
    rests = Restaurant.objects.all()
    context = {'rests': rests}
    return render(request, 'rests.html', context)


def detailed_rest(request, id):
    rest = Restaurant.objects.get(pk=id)
    context = {'rest': rest,
               'dishes': rest.dishes.all()
               }
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


def add_dish(request, id):
    rest = get_object_or_404(Restaurant, pk=id)
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.rest = rest
            dish.save()
            return redirect('detailed_rest')
    else:
        form = DishForm
    context = {'form': form}
    return render(request, 'add_dish.html', context)
