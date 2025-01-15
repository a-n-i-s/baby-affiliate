from django.shortcuts import render

# Create your views here.

def productlist(request):
    return render(request, 'product/product_list.html',context={})


def productdetail(request,pk):
    print(pk)
    return render(request, 'product/product_detail.html',{ 'id': pk })
