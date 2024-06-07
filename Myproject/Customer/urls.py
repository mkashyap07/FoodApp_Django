from django.urls import path
from Customer import views
app_name='Customer'

urlpatterns = [

    path('',views.web2,name='web2'),
    path('web2/ordernow/',views.orderNow,name='orderNow'),
    path('web2/ordernow/zomato/',views.zomato,name='zomato'),
]