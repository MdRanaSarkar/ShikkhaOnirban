from django.urls import path
from AppUser.views import user_login,user_panel,user_logout,user_register#,user_update
urlpatterns = [
	path('login/',user_login,name='user_login'),
	path('logout/',user_logout,name='user_logout'),
	path('register/',user_register,name='user_register'),
	path('user_panel/',user_panel,name='user_panel'),
	#path('user_update/',user_update,name="user_update"),
]