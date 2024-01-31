from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    published_date = models.DateField(auto_now_add=True)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='genres',null=True)


class BookDetail(models.Model):
    book_id = models.OneToOneField(Book,on_delete=models.CASCADE,related_name = 'details',null=True)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

