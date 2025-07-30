from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Menu, MenuItem
from .forms import MenuItemForm, UpdatePriceForm


# Create your views here.


class MenuListView(ListView):
    model = Menu
    template_name = "menus.html"
    context_object_name = "menus"


class MenuDetailView(DetailView):
    model = Menu
    template_name = "menu_detail.html"
    context_object_name = "menu"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.items.all()
        return context


class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "menuitem_form.html"

    def get_success_url(self):
        return reverse_lazy("menu_detail", kwargs={"pk": self.object.menu.id})


class MenuItemUpdatePriceView(UpdateView):
    model = MenuItem
    form_class = UpdatePriceForm
    template_name = "update_price.html"

    def get_success_url(self):
        return reverse_lazy("menu_detail", kwargs={"pk": self.object.menu.id})
