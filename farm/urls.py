from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('product/', product, name='product'),
    path('blog/', blog, name='blog'),
    path('detail/', detail, name='detail'),
    path('feature/', feature, name='feature'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
]
