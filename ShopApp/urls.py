from django.urls import  path
from ShopApp.views import Productview,product_single

urlpatterns=[
path('product/',Productview,name='product'),
path('product/<int:id>/',product_single,name='product_single')
]