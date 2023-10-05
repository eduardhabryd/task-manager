from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from tasks.forms import TaskCreateForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
	model = Task
	template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
	model = Task
	form_class = TaskCreateForm
	success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
	model = Task
	fields = "__all__"
	success_url = reverse_lazy("tasks:index")


class TagListView(generic.ListView):
	model = Tag


class TagCreateView(generic.CreateView):
	model = Tag
	fields = "__all__"
	success_url = reverse_lazy("tasks:tags")


class TagUpdateView(generic.UpdateView):
	model = Tag
	fields = "__all__"
	success_url = reverse_lazy("tasks:tags")