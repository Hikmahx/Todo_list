from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo

# Create your views here.
def index(request):
    #return HttpResponse("it is working!")
    listed = Todo.objects.all().order_by("-added_date")
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

def add_item(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_object=Todo.objects.create(added_date=current_date, text=content)
    print(created_object)
    print(created_object.id)
    return render(request, 'Todo_app/index.html')