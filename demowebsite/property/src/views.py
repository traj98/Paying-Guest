
from django.shortcuts import render
from .models import Property, Category

# Create your views here.
def Property_list(request):
	Property_list = Property.objects.all() 
	context = {

		'Property_list' : Property_list
	}


	return render(request, 'src/property-list.html',context)


def Property_detail(request, id):
	Property_detail =  Property.objects.get(id=id)

	context = {

		'Property_detail' : Property_detail

	}
	return render(request, 'src/detail.html',context)



def login(request):
	return render(request,'src/login.html')


def signup(request):
	return render(request,'src/signup.html')

def aboutus(request):
	return render(request,'src/about-us.html')



def contact(request):
	
	return render(request,'src/contact.html')