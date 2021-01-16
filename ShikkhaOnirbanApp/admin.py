from django.contrib import admin

# Register your models here.
from ShikkhaOnirbanApp.models import Setting, Category, SlideImages, Course, CourseImages, Event, EventImages, About,ContactMessage,Subject

admin.site.register(Setting)


# for category creating admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'status', 'keywords']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)

# it design for sliding images


class SlideImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(SlideImages, SlideImagesAdmin)

# for courseadminn creating admin panel


class Courseadmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course, Courseadmin)


# it's for the event admin design


class Eventadmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Event, Eventadmin)



class Aboutadmin(admin.ModelAdmin):
    list_display = ['title','created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(About, Aboutadmin)



admin.site.register(ContactMessage)

admin.site.register(Subject)