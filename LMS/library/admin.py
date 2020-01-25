from django.contrib import admin
from .models import Library,Librarian,Member,Book,Record


class libraryAdmin(admin.ModelAdmin):
    list_display = ('library_name','library_location',)

admin.site.register(Library,libraryAdmin)

class librarianAdmin(admin.ModelAdmin):
    list_display = ('librarian_name','library_name',)

admin.site.register(Librarian,librarianAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','isbn','no_of_copies','stock','available','is_returned','author_name')

admin.site.register(Book,BookAdmin)


class MemeberAdmin(admin.ModelAdmin):
    list_display = ('member_name','member_email','member_contact','member_address')


admin.site.register(Member, MemeberAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('member','date_of_issue','date_of_return','date_of_returned','issuing_librarian')


admin.site.register(Record, RecordAdmin)


# Register your models here.
