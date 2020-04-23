from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo

# Create your views here.
def index(request):
    #return HttpResponse("it is working!")
    listed = Todo.objects.all().order_by("-added_date")#orders by descending order
    context ={
        "listed": listed
    }
    return render(request, 'Todo_app/index.html', context)#returns the html file if its the request, context is the context of the page 

def details(request, id):
    items = Todo.objects.get(id=id)#gets an instance of the class Todo
    context = {
        'items': items #returns items from the list as of in the html for loop
    }
    return render(request, 'Todo_app/details.html', context)

def add_item(request):
    current_date = timezone.now()#the time the object was created
    content = request.POST["content"]#from name(content) in form, request.POST shows/post a request, ie returns a dict of the content input by the user {content: input data}
    created_object=Todo.objects.create(added_date=current_date, text=content)#to create new instances of Todo class
    return HttpResponseRedirect("/")#to go back to home/index page after creating instance