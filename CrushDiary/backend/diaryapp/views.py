from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Entry, Diary, User, SignInDetail, Locker, Memo 
from .serializers import EntrySerializer, DiarySerializer, UserSerializer, SignInDetailSerializer, LockerSerializer, MemoSerializer, SignUpSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SignInDetail
from .serializers import SignInDetailSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignInDetailViewSet(viewsets.ModelViewSet):
    queryset = SignInDetail.objects.all()
    serializer_class = SignInDetailSerializer

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class CreateUserAPIView(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        signin_detail = serializer.save()
        token, _ = Token.objects.get_or_create(user=signin_detail)
        return Response(
            {"token": token.key, "email": signin_detail.email},
            status=status.HTTP_201_CREATED
        )

class LogoutUserAPIView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
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