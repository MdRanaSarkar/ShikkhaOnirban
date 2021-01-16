from django.shortcuts import render
from ShopApp.models import Product,Images
from ShikkhaOnirbanApp.models import Setting, Category

# Create your views here.
def Productview(request):
	products=Product.objects.all()
	setting = Setting.objects.get(id=1)
	context={'products':products,
	'setting': setting,
	}
	return render(request,'products.html',context)




def product_single(request,id):
	product_sing=Product.objects.get(id=id)
	setting = Setting.objects.get(id=1)
	products=Product.objects.all().order_by('id')[:4]
	images=Images.objects.filter(product_id=id)
	context={
	'setting': setting,
	'product_sing':product_sing,
	'products':products,
	'images':images

	}
	return render(request,'products-single.html',context)

