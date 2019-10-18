from django.contrib import admin
from .models import Book, Author, Book_Issue, Customer
from django import forms


# Register your models here.
class AuthorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        author = self.cleaned_data.get('f_name')
        if len(author) < 4:
            raise forms.ValidationError("author name cannot be less than 4", code='error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(AuthorAdminForm, self).save(commit=commit)

class BookAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        b_name=self.cleaned_data.get('book_name')
        if len(b_name)<4:
            raise forms.ValidationError('book name should not be less than 4',code='error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(BookAdminForm,self).save(commit=commit)

class CustomerAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(CustomerAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        cust_name=self.cleaned_data.get('cust_name')
        if len(cust_name)<4:
            raise forms.ValidationError('customer name should not be less than 4',code='error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(CustomerAdminForm,self).save(commit=commit)


class BookIssueAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookIssueAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        book = self.cleaned_data.get('book')

        if book.stock == 0:
             if self.cleaned_data.get('is_returned') == False:

                 raise forms.ValidationError('stock is low so cannot issue book',code='error')
        return self.cleaned_data


    def save(self, commit=True):
        return super(BookIssueAdminForm,self).save(commit=commit)


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'book_price', 'no_of_copies', 'available', 'stock',  ]
    search_fields = ('book_name', 'stock', 'author',)
    form = BookAdminForm


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('f_name',)
    form = AuthorAdminForm


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cust_name', 'cust_no',)
    form =CustomerAdminForm

class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('issued_to',)
    form= BookIssueAdminForm


admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.register(Customer, CustomerAdmin)

admin.site.register(Book_Issue, BookIssueAdmin)