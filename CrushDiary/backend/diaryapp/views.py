from django.shortcuts import render
from rest_framework import status, viewsets, generics, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import Entry, Diary, CustomUser, Locker, Memo, PlayerCharacter
from .serializers import (
    EntrySerializer,
    DiarySerializer,
    UserSerializer,
    LockerSerializer,
    MemoSerializer,
    PlayerCharacterSerializer,
    CustomAuthTokenSerializer,
    PlayerCharacter
)

User = get_user_model()

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(diaryId__playerCharacterId__user=user)

    def perform_create(self, serializer):
        user = self.request.user
        diary_id = self.request.data.get('diaryId')
        
        if diary_id:
            serializer.save(diaryId_id=diary_id)  # Save diaryId directly
        else:
            raise serializers.ValidationError("Diary ID is required.")

class MoodChoicesView(APIView):
    def get(self, request):
        mood_choices = Entry.MOOD_CHOICES
        choices = [{'value': choice[0], 'label': choice[1]} for choice in mood_choices]
        return Response(choices)

class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Diary.objects.filter(playerCharacterId__user=user)  # Adjust according to your model relationships

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PlayerCharacterViewSet(viewsets.ModelViewSet):
    queryset = PlayerCharacter.objects.all()
    serializer_class = PlayerCharacterSerializer

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Check if the email or username already exists
        if CustomUser.objects.filter(email=request.data.get('email')).exists():
            return Response({"email": ["A user with this email already exists."]}, status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(username=request.data.get('username')).exists():
            return Response({"username": ["A user with that username already exists."]}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user first
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Prepare the PlayerCharacter data, using user.pk for the user field
        player_character_data = {
            'user': user.pk,  # Use the user's primary key (ID) instead of the user instance
            'inGameName': request.data.get('inGameName'),
            'eyeColour': request.data.get('eyeColour'),
            'hairColour': request.data.get('hairColour'),
        }

        # Create the PlayerCharacter
        player_character_serializer = PlayerCharacterSerializer(data=player_character_data)
        player_character_serializer.is_valid(raise_exception=True)
        player_character = player_character_serializer.save()  # Save the player character

        # Create the Diary and Locker
        diary = Diary.objects.create(author=player_character.inGameName, playerCharacterId=player_character)
        Locker.objects.create(diaryId=diary)  # Create a locker associated with the diary

        # Return user and diary information in the response
        return Response({
            "user": user_serializer.data,
            "diary_id": diary.diaryId  # Include the diary ID in the response
        }, status=status.HTTP_201_CREATED)



    
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)

        # Attempt to get the player's character and the associated diary
        player_character = PlayerCharacter.objects.filter(user=user).first()
        if not player_character:
            return Response({"error": "No associated player character found"}, status=404)

        diary = Diary.objects.filter(playerCharacterId=player_character).first()
        diary_id = diary.diaryId if diary else None

        # Create or retrieve the token
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'userId': user.id,
            'email': user.email,
            'diary_id': diary_id  # Include the diary ID in the response
        })
    
# class LoginView(APIView):
#     def post(self, request):
#         identifier = request.data.get('identifier')
#         password = request.data.get('password')

#         # Try to authenticate by username or email
#         user = authenticate(request, username=identifier, password=password)
#         if user is None:
#             try:
#                 # Try to get user by email if username fails
#                 user = User.objects.get(email=identifier)
#                 if user.check_password(password):
#                     user = authenticate(request, username=user.username, password=password)
#             except User.DoesNotExist:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#         if user is not None:
#             # Generate token and return response
#             token = ...  # Generate token here (use Django REST Framework JWT or similar)
#             return Response({'token': token}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class LogoutUserAPIView(APIView):
#     def get(self, request, format=None):
#         if request.user.is_authenticated:
#             request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

# class CustomAuthToken(APIView):
#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         try:
#             user = User.objects.get(email=email)  # Fetch user by email
#             if user.check_password(password):  # Verify the password
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
# class CurrentUserDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Assuming the email is unique and matches the logged-in user
#         sign_in_detail = SignInDetail.objects.get(email=request.user.email)
#         serializer = SignInDetailSerializer(sign_in_detail)
#         return Response(serializer.data)  # This will now return only the email
    

# class EntryListCreate(APIView):
#     def get(self, request):
#         entries = Entry.objects.all()
#         serializer = EntrySerializer(entries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EntrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EntryDetail(APIView):
#     def get(self, request, pk):
#         try:
#             entry = Entry.objects.get(pk=pk)
#             serializer = EntrySerializer(entry)
#             return Response(serializer.data)
#         except Entry.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# def CreateMemo(self,User,Crush):

#     f
#     name=User.name
#     eyeColour=User.eyeColour
#     hairColour=User.hairColour
#     Crush.matching