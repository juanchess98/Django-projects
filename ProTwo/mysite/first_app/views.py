from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord, User
# Create your views here.

def index(response):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    
    return render(request=response, template_name='first_app/index.html', context=date_dict)  

def help(response):
    help_dict = {'help_insert' : 'HELP PAGE !'}
    return render(response, 'first_app/help.html', help_dict)

def users(response):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users': users_list}
    return render(response, 'first_app/user.html', context=user_dict)   