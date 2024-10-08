"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from todos.views import TodoListView
from todos.views import TodoCreateView, TodoUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", TodoListView.as_view(), name="todo_list"
    ),  # quando for no caminho vazio, abre o todo.view
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="update_view"),
]  # int pk e para dizer que é um iteiro, já q é 0o id, e q e uma chave primaria
