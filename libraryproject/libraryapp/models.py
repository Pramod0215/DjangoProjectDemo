from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


class Author(models.Model):
    f_name = models.CharField(max_length=200)

    def __str__(self):
        return self.f_name

    # def get_author(self):
    #     return self.f_name

class Book(models.Model):
    available = models.BooleanField(default=True)
    book_name = models.CharField(max_length=200)
    book_price = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    stock=models.IntegerField(default=1)
    no_of_copies = models.IntegerField(default=1)
    # available_books = models.IntegerField(default=5)
    # isbn = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name

    # def get_b_name(self):
    #     return self.book_name

    def get_author(self):
        return self.author

# class Author(models.Model):
#     f_name=models.CharField(max_length=200)
#     l_name=models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.f_name

# def borrow(self):


class Customer(models.Model):
    cust_name = models.CharField(max_length=200)
    cust_no = models.IntegerField(default=0)
    customer_age = models.IntegerField(default=18)

    def __str__(self):
        return self.cust_name

    class Meta:
        managed=True

class Book_Issue(models.Model):
    issued_to = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # book_to_issue = models.ForeignKey('Book',null=True,on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_returned=models.BooleanField(default=False)

#
@receiver(pre_save, sender=Book_Issue)
def is_returned(sender, instance, **kwargs):
    stock = instance.book.stock
    if instance.is_returned:
        if instance.book.no_of_copies > stock:
            stock = stock + 1
            book = instance.book
            instance.is_returned = True
            book.stock = stock
            if stock > 0:
                book.availability = True
            book.save()


@receiver(post_save, sender=Book_Issue)
def borrowed(sender, instance, **kwargs):
    book = instance.book
    if instance.is_returned:
        book.stock = book.stock + 1
        book.save()
    else:
        if book.stock >= 0:
            book.stock = book.stock-1
        else:
            book.stock = 0
        book.save()

# @receiver(pre_save, sender=Book_Issue)
# def returned_books(sender, instance, **kwargs):
#     book = instance.book
#     if instance.is_returned:
#         if instance.book.available_books > book.stock:
#             book.stock += 1
#             book.save()

