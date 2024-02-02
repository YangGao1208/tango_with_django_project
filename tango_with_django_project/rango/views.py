from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage':'Crunchy,creamy,cookie,candy,cupcake!'}
    # return HttpResponse("Rango says hey there partner")
    return render(request, 'index1.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage':'This is writing by Yang Gao'}
    # return HttpResponse("Rango says here is about page")
    return render(request, 'about.html', context=context_dict)
