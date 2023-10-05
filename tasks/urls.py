from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from tasks import views

urlpatterns = [
	path("", views.TaskListView.as_view(), name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "tasks"
