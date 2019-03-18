from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from RNG.webhose_search import run_query

from RNG.models import Category, Game
from RNG.forms import CategoryForm, UserForm, UserProfileForm

from datetime import datetime 

def index(request):
    context_dict={}
    return render(request, 'RNG/index.html', context=context_dict)

def about(request):
    context_dict={}
    return render(request, 'RNG/about.html', context=context_dict)

def category(request):
    context_dict={}
    return render(request, 'RNG/category.html', context=context_dict)

def signup(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			
			profile.save()
			
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request,
				'RNG/signup.html',
				{'user_form': user_form,
				'profile_form': profile_form,
				'registered': registered},
				)
				
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your RNG account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
			
	else:
		return render(request, 'RNG/signin.html', {})
		
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def game(request):
    context_dict={}
    return render(request, 'RNG/game.html', context=context_dict)

def search(request):
    result_list=[]
    query=None
    if request.method == 'POST':
        query=request.POST['query'].strip()
        if query:
            #runs webhose search function
            result_list = run_query(query)
    return render(request,'RNG/search.html',{'result_list':result_list,'search_query':query})

def show_category(request, category_name_slug):
	context_dict={}
	try:
		category=Category.objects.get(slug=category_name_slug)
		pages = Game.objects.filter(category=category)
		context_dict['pages']=pages
		context_dict['category']=category
	except Category.DoesNotExist:
		context_dict['category']=None
		context_dict['pages']=None
	context_dict['query']=category.name
	result_list=[]
	if request.method=='POST':
		query=request.POST['query'].strip()
		if query:
			result_list=run_query(query)
			context_dict['query']=query
			context_dict['result_list']=result_list
	return render(request, 'RNG/category.html', context_dict)
