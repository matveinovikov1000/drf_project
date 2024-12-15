from rest_framework import serializers

from materials.models import Course, Lesson


class LessonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailModelSerializer(serializers.ModelSerializer):
    len_lessons_with_some_course = serializers.SerializerMethodField()
    lessons = LessonModelSerializer(many=True)

    def get_len_lessons_with_some_course(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = (
            "name",
            "preview",
            "description",
            "lessons",
            "len_lessons_with_some_course",
        )
