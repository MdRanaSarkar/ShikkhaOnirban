from django.contrib import admin

# Register your models here.
from ShopApp.models import Product,Images

class productImageInline(admin.TabularInline):
	model=Images
	extra=5

class ProductAdmin(admin.ModelAdmin):
	list_display=['title','status','created_at','updated_at','image_tag']
	list_filter=['title','created_at']
	list_per_page=10
	search_fields=['title','new_price','detail']
	readonly_fields=('image_tag',)
	inlines=[productImageInline]
	prepopulated_fields={'slug':('title',)}

admin.site.register(Product,ProductAdmin)