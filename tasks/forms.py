from django import forms

from tasks.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
	content = forms.CharField(
		max_length=1024,
		required=True,
		widget=forms.TextInput(
			attrs={
				"class": "form-control mb-3",
			}
		)
	)

	deadline = forms.DateTimeField(
		required=True,
		widget=forms.DateTimeInput(
			attrs={
				"class": "form-control mb-3",
				"type": "datetime-local"
			}
		)
	)

	done = forms.BooleanField(
		required=False,
		initial=False,
		widget=forms.CheckboxInput(
			attrs={
				"class": "hidden"
			}
		)
	)

	tags = forms.ModelMultipleChoiceField(
		queryset=Tag.objects.all(),
		widget=forms.CheckboxSelectMultiple(
			attrs={
				"class": "form-check mb-3",
			}
		)
	)

	class Meta:
		model = Task
		fields = ("content", "deadline", "done", "tags")
