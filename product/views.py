from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# Create your views here.
class ProductList(ListView):
    model=Product
    context_object_name="products"
    paginate_by=20



def productdetail(request,pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return render(request,'error.html',{'error_message':'404 Product not found'})
    return render(request, 'product/product_detail.html',{ 'product': product })
