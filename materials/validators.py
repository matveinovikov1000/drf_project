from rest_framework.serializers import ValidationError


def validate_link_video_lesson(value):
    if "youtube.com" not in value.lower():
        raise ValidationError("Может быть использована ссылка только на youtube.com")
