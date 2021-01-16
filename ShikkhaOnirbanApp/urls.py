from django.urls import path
from .views import Home,all_event,singlevent,About_main,Course_all,Course_single,contact

urlpatterns=[
    path('',Home,name='home'),
    path('about/',About_main,name='about'),
    path('event/',all_event,name='all_event'),
    path('single_event/<int:id>',singlevent,name='single_event'),
    path('course/',Course_all,name='Course_all'),
    path('course/<int:id>',Course_single,name='Course_single'),
    path('contact/',contact,name='contact_dat'),

]