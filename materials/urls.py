from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views import (
    CourseModelViewSet,
    LessonCreateAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    SubscriptionCreateAPIView,
)

app_name = MaterialsConfig.name

router = routers.SimpleRouter()
router.register("", CourseModelViewSet)

urlpatterns = [
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson"),
    path("lessons/", LessonListAPIView.as_view(), name="lessons"),
    path("lesson_create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lesson_update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lesson_delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path("subs_create/", SubscriptionCreateAPIView.as_view(), name="subs_create"),
] + router.urls
