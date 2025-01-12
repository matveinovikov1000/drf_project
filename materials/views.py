from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscription
from materials.serializers import (CourseDetailModelSerializer,
                                   LessonModelSerializer,
                                   SubscriptionModelSerializer)
from users.permissions import IsModerators, IsOwner
from materials.paginators import CustomPagination
from materials.tasks import add_mail


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailModelSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        course = serializer.save()
        add_mail.delay(course_id=course.id)

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
    pagination_class = CustomPagination


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


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionModelSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("courses")
        course_item = get_object_or_404(Course, pk=course_id)

        if Subscription.objects.filter(owner=user, courses=course_item).exists():
            Subscription.objects.get(owner=user, courses=course_item).delete()
            message = "Подписка удалена"
        elif not Subscription.objects.filter(owner=user, courses=course_item).exists():
            Subscription.objects.create(owner=user, courses=course_item, is_subs=True)
            message = "Подписка добавлена"
        return Response({"message": message})
