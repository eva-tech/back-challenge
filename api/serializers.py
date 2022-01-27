from api.models import Study
from rest_framework import serializers


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = [
            "id",
            "urgency_level",
            "body_part",
            "description",
            "type"
        ]
