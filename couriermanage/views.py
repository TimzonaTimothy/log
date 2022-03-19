from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import Courier
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

def home(request):
	
	return render(request, 'log/index-demo-1.html', {})

def search(request):
	user = request.user
	couriers = Courier.objects.filter()
	
	query = request.GET.get('q')
	if query:
		couriers = Courier.objects.filter(
			Q(tracking_id__icontains=query) | Q(phone__icontains=query) |
			Q(service__icontains=query)
			)
	Couriers = Courier.objects.order_by('-list_date')
	paginator = Paginator(couriers, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'log/search.html', {'page_obj':page_obj})


def main(request):
	user = request.user
	couriers = Courier.objects.filter(user=user)
	
	query = request.GET.get('q')
	if query:
		couriers = Courier.objects.filter(
			Q(tracking_id__icontains=query) | Q(phone__icontains=query) |
			Q(service__icontains=query)
			).order_by('-list_date')

	paginator = Paginator(couriers, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'couriermanage/main.html', {'page_obj': page_obj})


def listing(request, id=None):

    listing = get_object_or_404(Courier, id=id)
    context = {
        'listing':listing
    }

    return render(request, 'log/listing.html', context)

def about(request):
	return render(request, 'log/about-us.html', {})

def services(request):
	return render(request, 'log/services.html', {})

def faq(request):
	return render(request, 'log/faq.html', {})

def contact(request):
	return render(request, 'log/contact-us.html', {})


def sign_in(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	else:
			
		if request.method == 'POST':
			username = request.POST['Username']
			password = request.POST['Password']

			user = auth.authenticate(username=username, password=password)

			if user is not None:
				auth.login(request,user)
				messages.success(request, 'Login Success')
				return HttpResponseRedirect(reverse('main')) 
			else:
				messages.error(request, 'Invalid credentials')
				return redirect('/login')
		else:
			return render(request, 'log/login.html',{})
		


def register(request):
	if request.user.is_authenticated:
		return redirect('home')
    
   
	else:

		if request.method == 'POST':
			first_name = request.POST['firstname']
			last_name = request.POST['lastname']
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password1']
			password2 = request.POST['password2']
		

			if password==password2:
				if User.objects.filter(email=email).exists():
					messages.warning(request, 'Email Taken')
					return redirect('/register')
				elif User.objects.filter(username=username).exists():
					messages.warning(request, 'Username Taken')
					return redirect('/register')
				else:
					user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name,last_name=last_name,)
					user.save();
					messages.success(request, 'You are now registered and can log in')
					print('user created')
					return redirect('/login')

			else:
				messages.warning(request, 'Password Not Matching')
				return HttpResponseRedirect('/register')
			return HttpResponseRedirect('/register')

		else:
			return render(request, 'log/register.html', {})


  
	


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
