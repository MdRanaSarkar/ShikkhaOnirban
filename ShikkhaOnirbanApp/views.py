from django.shortcuts import render,HttpResponseRedirect,reverse
from ShikkhaOnirbanApp.models import Setting, Category, SlideImages, Course, CourseImages, Event, EventImages, About,ContactMessage,ContactForm
from django.contrib import messages
# Create your views here.


def Home(request):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    slideImages = SlideImages.objects.all()
    course = Course.objects.all()
    upcoming_event=Event.objects.all().order_by('id')[:3]
    event=Event.objects.all()
    about=About.objects.get(id=1)
    context = {'setting': setting,
               'category': category,
               'slideImages': slideImages,
               'course':course,
               'upcoming_event':upcoming_event,
               'event':event,
               'about':about,
               }
    return render(request, 'home.html', context)

#its the main about method
def About_main(request):
  about=About.objects.get(id=1)
  setting = Setting.objects.get(id=1)
  context={
  'setting': setting,
  'about':about,

  }
  return render(request, 'about_main.html', context)


#this is for the course part
def Course_all(request):
  course = Course.objects.all()
  setting = Setting.objects.get(id=1)
  context={
  'setting': setting,
  'course':course,

  }
  return render(request, 'course_all.html', context)

#this is for the course part
def Course_single(request,id):
  course = Course.objects.get(id=id)
  setting = Setting.objects.get(id=1)
  feature_Course=Course.objects.all().order_by('id')[:3]
  related_Course=Course.objects.all().order_by('-id')[:2]
  context={
  'setting': setting,
  'course':course,
  'feature_Course':feature_Course,
  'related_Course':related_Course,

  }
  return render(request, 'course_single.html', context)


#it is the for all event
def all_event(request):
  setting = Setting.objects.get(id=1)
  all_event=Event.objects.all()
  context={
  'setting': setting,
  'all_event':all_event,

  }
  return render(request,'event_all.html',context)

#its for the single event:
def singlevent(request,id):
  single_event=Event.objects.get(id=id)
  setting = Setting.objects.get(id=1)
  context={
  'setting': setting,
  'single_event':single_event,

  }
  return render(request,'event_single.html',context)




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your message has been sent')

            return HttpResponseRedirect(reverse('contact_dat'))

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    # category=Category.objects.all()
    context = {
        'setting': setting, 'form': form  # ,'category':category,
    }
    return render(request, 'contact_form.html', context)