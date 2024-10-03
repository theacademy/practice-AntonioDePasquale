from rest_framework import serializers
from .models import User, Diary, Entry, Locker, Memo, PlayerCharacter, CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import CustomUser




class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['diaryId', 'title', 'content', 'mood']  # Include the fields you need



class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['diaryId', 'author', 'playerCharacterId', 'noOfEntries']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']  # Include username if it's required
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data.get('username', None)  # Handle username if provided
        )
        user.set_password(validated_data['password'])  # Set password using set_password
        user.save()
        return user


class PlayerCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCharacter
        fields = ['user', 'inGameName', 'eyeColour', 'hairColour']

class LockerSerializer(serializers.ModelSerializer):
    """Serializer for Locker model."""
    class Meta:
        model = Locker
        fields = '__all__'

class MemoSerializer(serializers.ModelSerializer):
    """Serializer for Memo model."""
    class Meta:
        model = Memo
        fields = '__all__'

User = get_user_model()

class CustomAuthTokenSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # This will hold either the username or email
    password = serializers.CharField()

    def validate(self, attrs):
        identifier = attrs.get('identifier')
        password = attrs.get('password')

        # Determine if identifier is email or username
        try:
            user = User.objects.get(email=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=identifier)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid username or email.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")

        attrs['user'] = user
        return attrs


# # Serializer for user registration (SignUp)
# class SignUpSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True, style={'input_type': 'password'})

#     class Meta:
#         model = SignInDetail  # Create based on SignInDetail model
#         fields = ('email', 'password')
#         write_only_fields = ('password',)

#     def create(self, validated_data):
#         signin_detail = SignInDetail.objects.create(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         # Create a corresponding User instance after the SignInDetail is created
#         User.objects.create(
#             email=signin_detail.email,  # Link email to User's email
#             username=signin_detail.email  # Set username as email for simplicity
#         )
#         return signin_detail
