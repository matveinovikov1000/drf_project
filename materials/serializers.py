from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_link_video_lesson


class LessonModelSerializer(serializers.ModelSerializer):
    link_video = serializers.CharField(validators=[validate_link_video_lesson], read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailModelSerializer(serializers.ModelSerializer):
    len_lessons_with_some_course = serializers.SerializerMethodField()
    lessons = LessonModelSerializer(many=True, read_only=True)
    is_subs = serializers.SerializerMethodField()

    def get_len_lessons_with_some_course(self, obj):
        return obj.lessons.count()

    def get_is_subs(self, obj):
        user = self.context.get("request").user
        return Subscription.objects.filter(owner=user, courses=obj).exists()

    class Meta:
        model = Course
        fields = (
            "name",
            "preview",
            "description",
            "lessons",
            "len_lessons_with_some_course",
            "is_subs",
        )


class SubscriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
