from rest_framework import serializers

from .models import Homework

class HomeworkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['name', 'end_time']


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class HomeworkPutSerializer(serializers.Serializer):
    homework = serializers.CharField(max_length=50)
    modified_homework = serializers.CharField(max_length=50)
    modified_end_time = serializers.DateTimeField()

class HomeworkDeleteSerializer(serializers.Serializer):
    homework = serializers.CharField(max_length=50)