from lib2to3.fixes.fix_input import context

from django.contrib.messages import success
from django.http import JsonResponse

from django.shortcuts import render



# Create your views here.

def contact_form(request):
    context = {'success': True ,'message': 'Contact from sent successfully.'}
    return JsonResponse(context)

def contact(request):
    return render(request, 'contact.html')