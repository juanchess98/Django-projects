import email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings")

import django

django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):
    
    for entry in range(n):
        # get the topic for the topic
        fake_name = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()
        
        #create the user
        user_inst= User.objects.get_or_create(first_name=fake_name, last_name=fake_lastname, email=fake_email)[0]
        user_inst.save()
    
if __name__ == '__main__':
    print('populating script!')
    populate(10)
    print('populating complete!')
        
        