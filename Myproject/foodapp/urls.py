from django.urls import path
from foodapp import views
app_name='foodapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    
    # path('home/',views.food,name='food'),
    path('add/',views.create_item,name='create_item'),
    # path('web2/',views.web2,name="web2"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete_item/<int:id>/',views.delete_item,name='delete_item'),
    
]
