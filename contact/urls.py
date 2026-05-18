from django.urls import path
from .views import index
from .views import contact

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
