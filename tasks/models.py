from django.db import models


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
		ordering = ["done", "datetime"]

	def get_tags(self):
		return ",".join(list(self.tags.all().values_list("name", flat=True)))

	def __str__(self):
		return self.content
