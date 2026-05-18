from django.shortcuts import render
from contact.models import *

# Create your views here.
def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj


# Create your views here.
def index(request):
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_footer = get_general_setting('about_myself_footer')

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')
