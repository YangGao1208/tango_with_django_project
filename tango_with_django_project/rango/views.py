from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

# Create your views here.
# def index(request):
#     context_dict = {'boldmessage':'Crunchy,creamy,cookie,candy,cupcake!'}
#     # return HttpResponse("Rango says hey there partner")
#     return render(request, 'index1.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage':'This is writing by Yang Gao'}
    # return HttpResponse("Rango says here is about page")
    return render(request, 'about.html', context=context_dict)

def index(request):
    Category_list = Category.objects.order_by('-likes')[:5]
    most_liked_categories = Category.objects.order_by('-likes')[:5]
    most_viewed_pages = Page.objects.order_by('-views')[:5]
    
    
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake'
    context_dict['Categories'] = Category_list
    context_dict['most_liked_categories'] = most_liked_categories
    context_dict['most_viewed_pages'] = most_viewed_pages
        
    
    return render(request, 'index1.html', context = context_dict)



def show_category(request, category_name_slug):
    
    context_dict = {}
    
    try:
        category = Category.objects.get(slug = category_name_slug)
        
        pages = Page.objects.filter(Category = category)
        
    
        
        
        context_dict['pages'] = pages
        context_dict['category'] = category
        
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
        
    return render(request, 'category.html', context = context_dict)
