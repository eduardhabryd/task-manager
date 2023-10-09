from django.db import models
from django.urls import reverse


class Tag(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"
		ordering = ["name"]

	def __str__(self):
		return self.name


class Task(models.Model):
	content = models.CharField(max_length=1024)
	created_at = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()
	done = models.BooleanField()
	tags = models.ManyToManyField(Tag, related_name="tasks")

	class Meta:
		verbose_name = "Task"
		verbose_name_plural = "Tasks"
		ordering = ["done", "created_at"]

	def get_tags(self):
		tags_list = list(self.tags.all().values_list("name", flat=True))
		return ", ".join(tags_list)

	def __str__(self):
		return self.content
