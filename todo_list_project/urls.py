
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo_list_app.views import TaskViewSet, TagViewSet
from todo_list_app import views


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]

