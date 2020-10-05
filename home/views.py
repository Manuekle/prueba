from django.shortcuts import render, redirect

# Create your views here.

def vista_home(request):
    return render(request, 'home.html', locals())

def vista_about(request):
    return render(request, 'about.html', locals())

def vista_services(request):
    return render(request, 'services.html', locals())

def vista_store(request):
    return render(request, 'store.html', locals())

def vista_contact(request):
    return render(request, 'contact.html', locals())

def vista_blog(request):
    return render(request, 'blog.html', locals())