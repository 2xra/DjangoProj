from django.shortcuts import redirect, render

#from pizzas.forms import TopicForm, EntryForm

from .models import Pizza,Topping

# Create your views here.
def homepage(request):
    return render(request, 'pizzas/homepage.html')