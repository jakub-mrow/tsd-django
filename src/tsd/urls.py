from django.conf.urls import include
from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("tasks", views.TaskViewSet, "task")
router.register("cars", views.CarViewSet, "car")

urlpatterns = [
    re_path("", include(router.urls)),
    path('hello-world', views.first_endpoint),
    path('filter-tasks', views.filter_tasks)
]