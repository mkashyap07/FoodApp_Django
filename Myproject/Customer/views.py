from django.shortcuts import render
from Customer.models import Order
from Customer.forms import OrderForms
# Create your views here.

def web2(request):
    # template=loader.get_template('web2.html')
    return render(request,'Customer/web2.html')
def orderNow(request):
    return render(request,'Customer/zomato.html')
def zomato(request):
    if request.methods=='post':
        uname=request.POST.get('uname')
        date=request.POST.get('date')
        email=request.POST.get('email')
        number=request.POST.get('number')
        food=request.POST.get('food')
        Restaurant=request.POST.get('Restaurant')
        drinks=request.POST.get('drinks')
        soups=request.POST.get('soups')
        dish=request.POST.get('dish')
        order=request.POST.get('order')
        zomato=Order(uname=uname,date=date,email=email,number=number,food=food,Restaurant=Restaurant,drinks=drinks,soups=soups,dish=dish,order=order)
        zomato.save()
    return render(request,'zomato.html')
