from django.shortcuts import render, redirect
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


class TaskDeleteView(generic.DeleteView):
	model = Task
	success_url = reverse_lazy("tasks:index")
	template_name = "tasks/task_confirm_delete.html"


def task_complete(request, pk):
	task = Task.objects.get(pk=pk)
	task.done = True
	task.save()
	return redirect("tasks:index")


def task_undo(request, pk):
	task = Task.objects.get(pk=pk)
	task.done = False
	task.save()
	return redirect("tasks:index")


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


class TagDeleteView(generic.DeleteView):
	model = Tag
	success_url = reverse_lazy("tasks:tags")
