# Library-management-system

In this app there are multiple libraries. In each library there are multiple librarians and books. So basically a member can borrow a book from the library only if he is a member.
Processes and Services:

  # Processes and Services:
  1. Book is issued by the librarian and then has to be returned within a due date of 7 days.
  2. If at all he doesn't return the book on or before the due date he is going to pay the fine as assigned by the library standards.
  3. I have implemented the concept of 
  
  ### post_save
so that as soon the book is returned it is shown available for the rest of the members of library.
4.A member can borrow only limited books from the library.

To run this in your system:

Clone this repo in your system:
```
git clone https://github.com/Pramod0215/Library-management-system/
```
Get inside the repo, type this is terminal:
```
cd Library-Management-System
```
Next step is to install all the dependencies into your virtual environment:
```
pip3 install 
Django==3.0.1
django-jsonfield==1.4.0
```
Next get into the project directory by typing:
```
cd LMS
```
Type 3 commands in order before for the project to run:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Now to access the admin page before running the server create a superuser:
```
python3 manage.py createsuperuser
fill the details :
username: <ur choice>
email: <optional>
password: <password>
confirm password: <confirm the password>
```
After filling all these to run the project:
```
python3 manage.py runserver
```
