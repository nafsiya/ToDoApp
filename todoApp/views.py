from django.shortcuts import render
from todoApp.serializers import  UserSerializer,TodoSerilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from todoApp.models import TodoModel


# # Create your views here.
# class UserCreateView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             # serializer.save() #User.objects.create(username="",email="",password="")
#             print(serializer.validated_data)
#             User.objects.create_user(**serializer.validated_data)
#             return Response({"msg":"student created successfully"})
#         else:
#             return Response(serializer.errors)

class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer
    
    def perform_create(self, serializer):  #ivide password encryption ullathkondaan ingane cheythath allenkil mukalilullath mathram mathi
        print("-------------------------------")
        return User.objects.create_user(**serializer.validated_data)
    
    
class TodoCreatedList(CreateAPIView,ListAPIView):
    serializer_class=TodoSerilizer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def perform_create(self, serializer):
        print("-----------------------")
        user=self.request.user
        return serializer.save(owner=user)
    
    def get_queryset(self):
        return TodoModel.objects.filter(owner=self.request.user)
    
class TodoRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=TodoSerilizer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=TodoModel.objects.all()
    lookup_url_kwarg="id"
    
    
class TodoCountView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        pending_count=TodoModel.objects.filter(owner=self.request.user,status="pending").count()
        compled_count=TodoModel.objects.filter(owner=self.request.user,status="completed").count() 
        return Response({"pending":pending_count,"completed":compled_count})
