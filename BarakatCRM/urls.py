from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # My Profile
    path('myprofile/',MyProfileView.as_view(),name='My-Profile'),
    # About Us
    path('aboutus',AboutUs.as_view(),name='About-Us'),
    # Products
    path('',ProductsView.as_view(),name='Base-Page'),
    path('addproduct',AddProduct.as_view(),name='Add-Product'),
    path('detailproduct/<int:pk>',DetailProduct.as_view(),name='Detail-Product'),
    path('editproduct/<int:pk>',EditProduct.as_view(),name='Edit-Product'),
    path('deleteproduct/<int:pk>',DeleteProduct.as_view(),name='Delete-Product'),
    # Clients
    path('clients',ClientsListView.as_view(),name='Clients-List'),
    path('addclient',AddClient.as_view(),name='Add-Client'),
    path('detailclient/<int:pk>',DetailClient.as_view(),name='Detail-Client'),
    path('editclient/<int:pk>',EditClient.as_view(),name='Edit-Client'),
    path('deleteclient/<int:pk>',DeleteClient.as_view(),name='Delete-Client'),
    # Sklad/Product/Category
    path('skladproducts',SkladProducts.as_view,name='Sklad-Products')

]
