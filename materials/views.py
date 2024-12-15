from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import (CourseDetailModelSerializer,
                                   LessonModelSerializer)
from users.permissions import IsModerators, IsOwner


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailModelSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action in "create":
            self.permission_classes = (~IsModerators,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerators | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerators | IsOwner,)

        return super().get_permissions()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerators | IsOwner,
    )


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerators | IsOwner,
    )


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    permission_classes = (
        IsAuthenticated,
        ~IsModerators,
    )

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerators | IsOwner,
    )


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    permission_classes = (
        IsAuthenticated,
        ~IsModerators | IsOwner,
    )
