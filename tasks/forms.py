from django import forms

from tasks.models import Task


# content = models.CharField(max_length=1024)
# 	datetime = models.DateTimeField()
# 	deadline = models.DateTimeField()
# 	done = models.BooleanField()
# 	tags = models.ManyToManyField(Tag, related_name="tasks")

class TaskCreateForm(forms.ModelForm):
	content = forms.CharField(
		max_length=1024,
		required=True,
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
			}
		)
	)

	class Meta:
		model = Task
		fields = "__all__"
