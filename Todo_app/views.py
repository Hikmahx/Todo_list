from django.shortcuts import render
from django.http import HttpResponse

from django.models import Todo

# Create your views here.
def index(request):
    #return HttpResponse("it is working!")
    listed = Todo.objects.get()
    context ={
        "text" : "text",
        "listed": listed
    }
    return render(request, 'Todo_app/index.html', context)