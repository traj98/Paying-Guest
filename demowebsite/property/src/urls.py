from django.urls import path
from . import views

app_name = 'src'

urlpatterns = [
	path('',views.Property_list,name='Property_list'),
	path('<int:id>detail/',views.Property_detail,name='Property_detail'),
	path('login/',views.login,name='login'),
	path('signup/',views.signup,name='signup'),
	path('aboutus/',views.aboutus,name='aboutus'),
	path('contact/',views.contact,name='contact'),



]