from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from tasks import views

urlpatterns = [
	path("", views.TaskListView.as_view(), name="index"),
	path("tags/", views.TagListView.as_view(), name="tags"),
	path("tags/create/", views.TagCreateView.as_view(), name="create-tag"),
	path("tags/<int:pk>/update", views.TagUpdateView.as_view(), name="tag-update"),
	path("tags/<int:pk>/delete", views.TagDeleteView.as_view(), name="tag-delete"),
	path("tasks/create/", views.TaskCreateView.as_view(), name="create-task"),
	path("tasks/<int:pk>/update", views.TaskUpdateView.as_view(), name="task-update"),
	path("tasks/<int:pk>/delete", views.TaskDeleteView.as_view(), name="task-delete"),
	path("tasks/<int:pk>/complete", views.task_complete, name="task-complete"),
	path("tasks/<int:pk>/undo", views.task_undo, name="task-undo"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "tasks"
