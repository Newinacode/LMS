from rest_framework import serializers
from .models import Book,BookDetail

class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookDetail
        fields = ['number_of_pages','publisher','language']

class BookSerializer(serializers.ModelSerializer):
    details = BookDetailSerializer()
    # history = BookDetailSerializer()
    class Meta:
        model = Book
        fields = ['id','title','ISBN','published_date','genre','details']


    def create(self,validated_data):
        details = validated_data.pop('details')
        book = Book.objects.create(**validated_data)
        BookDetail.objects.create(book_id=book,**details)
        return book


    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.ISBN = validated_data.get('ISBN', instance.ISBN)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        
        instance.save()
        detail_data = validated_data.get('details',{})
        

        if instance.details:
            detail_instance = instance.details
            details_serializer = BookDetailSerializer(detail_instance, data=detail_data)
            if details_serializer.is_valid():
                details_serializer.save()
        else:
            details_serializer = BookDetailSerializer(data=detail_data)
            if details_serializer.is_valid():
                details_serializer.save(book=instance)


        return instance

