from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .forms import TodoForm
from .models import Todo

def todo_form(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

class ToDoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_todo_url'] = 'todo_form'  # URL to redirect to the todo_form
        return context
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
