from rest_framework import serializers
from .models import User, Diary, Entry, SignInDetail, Locker, Memo 
from django.contrib.auth import get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer

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

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'

class CustomAuthTokenSerializer(AuthTokenSerializer):
    # You can customize your serializer here if needed
    pass

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = SignInDetail
        fields = ('email', 'password')
        write_only_fields = ('password',)
    def create(self, validated_data):
        signin_detail = SignInDetail.objects.create(
            email=validated_data['email'],
            password=validated_data['password']
        )
        User.objects.create(email=signin_detail, username=validated_data['email'])
        return signin_detail