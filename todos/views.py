from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView #ajuda na criação de view de listagem
from django.views.generic import ListView, CreateView

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]