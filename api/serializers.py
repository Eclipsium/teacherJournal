from rest_framework import serializers

from api.models import *


class StudentSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['math'] < 1 or data['math'] > 5 or \
                data['physic'] < 1 or data['physic'] > 5 or \
                data['russian'] < 1 or data['russian'] > 5 or \
                data['english'] < 1 or data['english'] > 5:
            raise serializers.ValidationError("Оценка должна быть от 1 до 5")
        return data

    class Meta:
        model = Student
        fields = [
            'id', 'name', 'math', 'physic', 'russian', 'english'
        ]
