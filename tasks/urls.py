from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from tasks import views

urlpatterns = [
	path("", views.TaskListView.as_view(), name="index"),
	path("tags/", views.TagListView.as_view(), name="tags"),
	path("tasks/create/", views.TaskCreateView.as_view(), name="create-task"),
	path("tasks/<int:pk>/update", views.TaskUpdateView.as_view(), name="task-update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "tasks"
