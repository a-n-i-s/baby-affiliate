
from django.urls import path
from .views import productlist,productdetail

urlpatterns = [
    path('', productlist, name='product-list'),
    path('<str:pk>', productdetail, name='product-detail'),

]
