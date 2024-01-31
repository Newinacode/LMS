from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from .models import Book,BookDetail
from .serializers import BookSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ModelViewSet):
    

    queryset = Book.objects.all()
    serializer_class = BookSerializer()



    @action(detail=False,methods=['get'])
    def list(self,request):
        data = BookSerializer(self.get_queryset(),many=True).data
        return Response(data=data)


    @action(detail=False,method=['post'])
    def create(self,request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Book has been created successfully'}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    @action(detail=True,method=["post"])
    def update(self,request,pk=None):
        book = get_object_or_404(Book,pk=pk)
        serializer = BookSerializer(data = request.data,instance=book)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"Book has been updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True,method=["delete"])
    def destory(self,request,pk=None):
        book = get_object_or_404(Book,pk=pk)
        book.delete()
        return Response({"data":"Book has been removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    

    @action(detail=True,method=['get'])
    def retrieve(self,request,pk=None):
        book = get_object_or_404(Book,pk=pk)
        serializer = BookSerializer(book)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)
