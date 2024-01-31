from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer()

    @action(detail=False,methods=['get'])
    def list(self,request):
        data = UserSerializer(self.get_queryset(),many=True).data
        return Response(data=data)


    @action(detail=False,method=['post'])
    def create(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'User has been created successfully'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    @action(detail=True,method=["post"])
    def update(self,request,pk=None):
        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(data = request.data,instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"User has been updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True,method=["delete"])
    def destory(self,request,pk=None):
        user = get_object_or_404(User,pk=pk)
        user.delete()
        return Response({"data":"User has been removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    

    @action(detail=True,method=['get'])
    def retrieve(self,request,pk=None):
        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(user)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)


        
