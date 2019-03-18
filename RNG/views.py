from django.shortcuts import render
from django.http import HttpResponse

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
    context_dict={}
    return render(request, 'RNG/signup.html', context=context_dict)

def game(request):
    context_dict={}
    return render(request, 'RNG/game.html', context=context_dict)
