from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    my_dictionary = {'insert_me': "Now i'm coming from first_app/index.html !"}
    return render(request=response, template_name='first_app/index.html', context=my_dictionary)  

def help(response):
    help_dict = {'help_insert' : 'HELP PAGE !'}
    return render(response, 'first_app/help.html', help_dict)