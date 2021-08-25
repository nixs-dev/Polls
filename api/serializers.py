from rest_framework import serializers
from polls.models import Question

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = '__all__'