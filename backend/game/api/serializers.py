from rest_framework import serializers
from game.models import PlayedGameBy

class AddUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedGameBy
        fields = '__all__'

class PlayGameSerializer(serializers.ModelSerializer):
    user_value = serializers.CharField()

class FinalResultSerializer(serializers.ModelSerializer):
    your_score = serializers.CharField()
    com_score = serializers.CharField()