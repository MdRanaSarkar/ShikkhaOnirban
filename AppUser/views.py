from django.shortcuts import render, HttpResponseRedirect, reverse,redirect
from ShikkhaOnirbanApp.models import Setting, Category, SlideImages, Course, CourseImages, Event, EventImages, About, ContactMessage, ContactForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from AppUser.forms import SignUpForm#,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
#from AppUser.models import UserProfile
# Create your views here.


# def Register(request):
# 	setting = Setting.objects.get(id=1)
# 	context={'setting':setting}
# 	return render(request,'accountLR.html',context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Your email or password is not valid")

    setting = Setting.objects.get(id=1)
    context = {  # 'category': category,
        'setting': setting}
    return render(request, 'user_login.html', context)



def user_panel(request):
	setting = Setting.objects.get(id=1)
	context={
'setting': setting
	}
	return render(request,'user_panel.html',context)



def user_logout(request):
	logout(request)
	return redirect('user_login')





def user_register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password_raw=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password_raw)
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Your new and reset password is not matching")
    else:
        form=SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={'category': category,
               'setting': setting,
               'form':form}
    return render(request,'user_register.html',context)





# @login_required(login_url='/user/login')  # Check login
# def user_update(request):
#     if request.method == 'POST':
#         # request.user is user  data
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(
#             request.POST, request.FILES, instance=request.user)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your account has been updated!')
#             return redirect('home')
#     else:
#        # category = Category.objects.all()
#         user_form = UserUpdateForm(instance=request.user)
#         # "userprofile" model -> OneToOneField relatinon with user
#         profile_form = ProfileUpdateForm(instance=request.user)
#         context = {
#             # 'category': category,
#             'user_form': user_form,
#             'profile_form': profile_form
#         }
#         return render(request, 'userupdate.html', context)
