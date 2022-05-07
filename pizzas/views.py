from django.shortcuts import redirect, render

from pizzas.forms import CommentForm

from .models import Pizza,Topping,Comment

from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'pizzas/homepage.html')


def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}
    
    return render(request, 'pizzas/pizzas.html', context)



def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    pizzaimg = 'pizzas/media/'+pizza.pizza_name+'.jpg'
    print(pizzaimg)
    toppings = pizza.topping_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments,'pizzaimg':pizzaimg}

    return render(request, 'pizzas/pizza.html', context)

@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.owner = request.user
            new_comment.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}

    return render(request, 'pizzas/new_comment.html', context)