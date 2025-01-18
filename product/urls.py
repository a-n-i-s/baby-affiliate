
from django.urls import path
from .views import ProductList,productdetail

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<str:pk>', productdetail, name='product-detail'),

]
