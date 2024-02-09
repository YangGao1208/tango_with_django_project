from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
from django.shortcuts import redirect
from django.urls import reverse
from rango.forms import UserForm, UserProfileForm
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



def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)
        
    return render(request, 'add_category.html' , {'form':form})




def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
        return redirect('/rango/')
    
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                
                return redirect(reverse('rango:show_category',kwargs={'category_name_slug':category_name_slug}))
            
        else:
            print(form.errors)
                
    context_dict = {'form': form, 'category': category}
            
    return render(request, 'add_page.html', context=context_dict)


def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save
            
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
        
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
        
    return render(request, 'rango/register.html', context = {'user_form' : user_form, 'profile_form': profile_form, 'registered': registered})
     