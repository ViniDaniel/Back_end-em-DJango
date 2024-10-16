from django.shortcuts import render
from .models import Todo
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)  # ajuda na criação de view de listagem
from django.urls import reverse_lazy


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
