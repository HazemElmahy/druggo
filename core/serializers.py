from rest_framework import serializers
from .models import Hello


class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hello
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Hello.objects.create(**validated_data)