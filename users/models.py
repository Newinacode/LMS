from django.db import models
from books.models import Book


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    membership_date = models.DateField(auto_now_add=True)


class BorrowedBook(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "user")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="books")
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
