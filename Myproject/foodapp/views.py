from django import template
from django.shortcuts import render,redirect
from django.template import loader
from foodapp.models import Contact2
# from django.http import HttpResponse
from foodapp.models import Item
from .forms import ItemForms
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return HttpResponse("Hello in my project's home page")
@login_required
def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,"index.html",context)

def detail(request,id):
    item=Item.objects.get(pk=id)
    context={
        'item':item,
    }
    return render(request,"detail.html",context)

def create_item(request):
    form=ItemForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foodapp:index')
    return render(request,'item-form.html',{'form':form})

def update(request,id):
    item=Item.objects.get(id=id)
    form=ItemForms(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('foodapp:index')
    return render(request,'item-form.html',{'form':form})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('foodapp:index')
    return render(request,'delete_msg.html',{'item.item_name':item.item_name})



