from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Entry, Diary, User, SignInDetail
from .serializers import EntrySerializer, DiarySerializer, UserSerializer, SignInDetailSerializer
from rest_framework import viewsets


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




