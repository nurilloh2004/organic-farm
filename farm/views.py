from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'all/index.html')

def about(request):
    return render(request, 'all/about.html')

def service(request):
    return render(request, 'all/service.html')

def product(request):
    return render(request, 'all/product.html')

def blog(request):
    return render(request, 'all/blog.html')

def detail(request):
    return render(request, 'all/detail.html')

def feature(request):
    return render(request, 'all/feature.html')

def team(request):
    return render(request, 'all/team.html')

def testimonial(request):
    return render(request, 'all/testimonial.html')

def contact(request):
    return render(request, 'all/contact.html')
