from rest_framework import serializers
from notes.models import User, Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'                             # Display all the fields that are part of the model


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'