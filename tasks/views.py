from django.shortcuts import render
from django.views import generic

from tasks.forms import TaskCreateForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
	model = Task
	template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
	model = Task
	form_class = TaskCreateForm

class TaskUpdateView(generic.UpdateView):
	model = Task
	fields = "__all__"


class TagListView(generic.ListView):
	model = Tag

