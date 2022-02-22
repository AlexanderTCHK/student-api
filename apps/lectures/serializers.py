from rest_framework import serializers
from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description', 'date',
                  'slides_url', 'created_at', 'updated_at')
