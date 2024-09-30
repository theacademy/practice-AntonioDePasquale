from rest_framework import serializers
from .models import User, Diary, Entry, SignInDetail

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SignInDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignInDetail
        fields = '__all__'