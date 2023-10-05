from django.db import models


# content - describes what you should do.
# datetime, when a task was created
# optional deadline datetime if a task should be done until some datetime
# the boolean field that marks if the task is done or not
# tags that are relevant for this task
# Tag - a tag symbolizes the theme of the task and consists only of a name.


class Tag(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"
		ordering = ["name"]

	def __str__(self):
		return self.name


class Task(models.Model):
	content = models.CharField(max_length=100)
	datetime = models.DateTimeField()
	deadline = models.DateTimeField()
	done = models.BooleanField()
	tags = models.ManyToManyField(Tag, related_name="tasks")

	class Meta:
		verbose_name = "Task"
		verbose_name_plural = "Tasks"
		ordering = ["datetime", "done"]

	def __str__(self):
		return self.content
