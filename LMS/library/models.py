from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Library(models.Model):
    library_name = models.CharField(max_length=100)
    library_location = models.CharField(max_length=100)
    # library_name = models.ForeignKey(Librarian, on_delete=100)

    def __str__(self):
        return self.library_name

class Librarian(models.Model):
    librarian_name = models.CharField(max_length=100)
    library_name = models.ForeignKey(Library,on_delete=models.CASCADE)

    def __str__(self):
        return self.librarian_name



class Member(models.Model):
    member_name = models.CharField(max_length=100)
    member_email = models.EmailField()
    member_contact = models.IntegerField()
    member_address = models.TextField()


    def __str__(self):
        return self.member_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    book_price = models.IntegerField()
    author_name = models.CharField(max_length=100)
    no_of_copies = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default= True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name

class Record(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    issuing_librarian = models.ForeignKey(Librarian,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    date_of_issue = models.DateField()
    date_of_return = models.DateField()
    date_of_returned = models.DateField()

    def __str__(self):
        return str(self.date_of_return)


# @receiver(pre_save, sender=Record)
# def is_returned(sender, instance, **kwargs):
#     stock = instance.book.stock
#     if stock.is_returned:
#         if instance.book.no_of_copies > stock:
#             stock += 1
#             book = instance.book
#             instance.is_returned = True
#             book.stock = stock
#             if stock > 0:
#                 book.availability = True
#             book.save()
#

@receiver(post_save, sender=Record)
def borrowed(sender, instance, **kwargs):
    book = instance.book
    if book.is_returned:
        book.stock = book.stock + 1
        book.save()
    else:
        if book.stock >= 0:
            book.stock = book.stock-1
        else:
            book.stock = 0
        book.save()
    if book.is_returned==True:
        book.stock = book.stock+1
        book.save()

