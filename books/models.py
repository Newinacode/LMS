from django.db import models
from users.models import User
class Book(models.Model):
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    published_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=20)
    in_library = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BookDetail(models.Model):
    book_id = models.OneToOneField(Book,on_delete=models.CASCADE,related_name = 'details',null=True)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=100)


    def __str__(self):
        return f"detail of {self.book_id.title}"



class BorrowedBook(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "user")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="books")
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True,default=None)

    class Meta: 
        ordering = ["-borrow_date"]

    def __str__(self):
        return f"{self.book_id.title} taken by {self.user_id.name} in {self.borrow_date}"


