
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings")

import django

django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, WebPage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', ' Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    
    for entry in range(n):
        # get the topic for the topic
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Create the new webpage entry
        webpg = WebPage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        #Create a fake access record for that webpag
        acc_rec = AccessRecord.object.get_or_create(name=webpg, date=fake_date)[0]
if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')
        
        
    
    