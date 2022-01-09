from rest_framework import serializers
from game.models import PlayedGameBy

class AddUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedGameBy
        fields = '__all__'

class PlayGameSerializer(serializers.Serializer):
    user_value = serializers.CharField()

class FinalResultSerializer(serializers.Serializer):
    your_score = serializers.CharField()
    com_score = serializers.CharField()