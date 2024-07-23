from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo.urls import router as todo_router
from todo.views import TodoViewSet

router = routers.DefaultRouter()
router.registry.extend(todo_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
