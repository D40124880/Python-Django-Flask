from djang.conf.urls import urls
from . import views
urlpatterns = [
    url(r'^$', views.index, name="my_index"),
    url(r'^this_app/new$', views.new, name="my_new"),
    url(r'^this_app(?P<id>\d+)/edit$', views.edit, name="my_edit"),
    url(r'^this_app(?P<id>\d+)/delete$', views.delete, name="my_delete"),
    url(r'^this_app(?P<id>\d+)$', views.show, name="my_show"),
]

# inside your app's index.html file
<a href="/target/this_app/new"></a>


<!-- is the equivalent of:  -->
<a href="{% url 'my_new' %}"></a>


<!-- This form's action attribute -->
<form class="" action="/target/this_app/5/delete" method="post">
  <input type="submit" value="Submit">
</form>


<!-- is the equivalent of: -->
<form class="" action="{%url 'my_delete' id=5 %}" method="post">
  <input type="submit" value="Submit">
</form>


------------------------------------------------------------------------------------------

from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    blog = models.ForeignKey(Blogs, related_name="comments")

class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    blogs = models.ManyToManyField(Blogs, related_name="admins")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)

    author = models.ForeignKey(Author, related_name="books")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

this_author = Author.objects.get(id=2)
my_book = Book.objects.create(title="Little Women", author=this_author)
# OR
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

# to search by is:
books = Book.objects.filter(author__name="Louise May Alcott")
books = Book.objects.filter(author__name__startswith="Lou")

#the following is for a reverse lookup
#  related_name

#to get all the books it is:
#  some_author.books.all()

------------------------------------------------------------------------------------------

class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# adding a relationship between two existing records is simple:
this_book = Book.obejcts.get(id=4)
this_publisher = Publisher.objects.get(id=2)
this_publisher.books.add(this_book)