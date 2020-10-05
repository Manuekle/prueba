from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_home, name = 'home'),
    path('about/', vista_about, name = 'about'),
    path('services/', vista_services, name = 'services'),
    path('store/', vista_store, name = 'store'),
    path('contact/', vista_contact, name = 'contact'),
    path('blog/', vista_blog, name = 'blog'),
]
