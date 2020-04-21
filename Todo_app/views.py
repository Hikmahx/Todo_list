from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.
def index(request):
    #return HttpResponse("it is working!")
    listed = Todo.objects.all()[:10]
    context ={
        "text" : "To do items",
        "listed": listed
    }
    return render(request, 'Todo_app/index.html', context)

def details(request, id):
    items = Todo.objects.get(id=id)

    context = {
        'items': items
    }
    return render(request, 'Todo_app/details.html', context)