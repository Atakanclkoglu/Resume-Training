from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from core.models import GeneralSetting, ImageSetting, Skill , Experience


# Create your views here.

def index(request):

    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    #IMAGES
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file


    #SKILLS
    skills = Skill.objects.all()

    experiences = Experience.objects.all().order_by('-start_date')


    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'home_banner_name': home_banner_name,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'skills': skills,
        'experiences': experiences,
    }

    return render(request, 'index.html',context=context)

