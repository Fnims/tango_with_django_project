import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
django.setup()
from rango.models import Category, Page

def populate():
    #first we will create lists of dictionaries containing the pages
    #we want to add in each category
    #then we create a dictionary of disctionaries for our categories
    #this allows us to iterate through eahc data structure and add teh data to our models


    python_pages = [
        {'title':'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/', 'views': 10},
        {'title':'How to Think like a Computer Scientist', 
         'url':'http://www.greenteapress.com/thinkpython/', 'views': 20},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/', 'views': 50} ]
    

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 60},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/', 'views': 5},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/', 'views': 90} ]
    

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/', 'views': 5},
        {'title':'Flask',
         'url':'http://flask.pocoo.org', 'views': 2} ]
    
    other_pages2 = [
        {'title':'testing', 
         'url': 'http://bottlepy.org/docs/dev/', 'views': 1}
    ]
    

    cats = {'Python':{'pages': python_pages, 'likes':64, 'views':128},
            'Django':{'pages': django_pages, 'likes':32, 'views':64},
            'Other Frameworks':{'pages': other_pages, 'likes':16, 'views':32},
            'Test Category':{'pages': other_pages2, 'likes': 10, 'views': 100} }
    


    #code below goes through the cats diction then adds each category
    #and then adds all teh assocated pages for that category
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['likes'], cat_data['views'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}: {p}')
    

def add_cat(name, likes, views):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c


def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
