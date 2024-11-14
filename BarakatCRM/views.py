from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import *

# My Profile

from django.views.generic import TemplateView

class MyProfileView(TemplateView):
    template_name = "my_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] =   self.request.user 
        return context


class MyProfileView(generic.DetailView):
    model = User
    context_object_name = 'user'  
    template_name = "my_profile.html"

    def get_object(self, queryset=None):
        return self.request.user


# About Us
class AboutUs(generic.TemplateView):
    template_name = "about_us.html"

# Products
class ProductsView(generic.ListView):
    model = Product
    template_name = "base.html"
    fields = "__all__"
    permission_required = "BaraktCRM.view_barakat"
    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)


class DetailProduct(generic.DetailView):
    model = Product
    template_name = "product_detail.html"

class AddProduct(generic.CreateView):
    model = Product
    fields = "__all__"
    template_name = 'product_form.html'
    success_url = reverse_lazy('Base-Page')


class EditProduct(generic.UpdateView):
    model = Product
    fields = "__all__"
    template_name = 'product_form.html'
    success_url = reverse_lazy('Base-Page')
    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)

class DeleteProduct(generic.DeleteView):
    model = Product
    fields = "__all__"
    template_name = 'confdelproduct.html'
    success_url = reverse_lazy('Base-Page')

# Clients 

class ClientsListView(generic.ListView):
    model = Client
    fields = "__all__"
    template_name = 'clients_list.html'
    def get_queryset(self):
        return Client.objects.filter(created_by=self.request.user)


class AddClient(generic.CreateView):
    model = Client
    fields = "__all__"
    template_name = 'clients_form.html'
    success_url = reverse_lazy('Clients-List')

class DetailClient(generic.DetailView):
    model = Client
    template_name = "client_detail.html"


class EditClient(generic.UpdateView):
    model = Client
    fields = "__all__"
    template_name = 'clients_form.html'
    success_url = reverse_lazy('Clients-List')

class DeleteClient(generic.DeleteView):
    model = Client
    fields = "__all__"
    template_name = 'confdelclient.html'
    success_url = reverse_lazy('Clients-List')

class SkladProducts(generic.ListView):
    model = SkladProducts
    fields = "__all__"
    template_name = 'sklad_products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sklad"] = Product.objects.filter(sklad = kwargs['pk'])
        return context
    


    