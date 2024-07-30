from django.shortcuts import render
from .forms import *
# Create your views here.

def register(request):
    ERFO = RegisterForm()
    d = {'ERFO': ERFO}
    return render(request, 'register.html', d)


def insert_topic(request):
    ETFO = TopicForm()
    d = {'ETFO':ETFO}
    return render(request, 'insert_topic.html', d)


def insert_author(request):
    EAFO = AuthorForm()
    d = {'EAFO': EAFO}
    return render(request, 'insert_author.html', d)

def insert_book(request):
    EBFO = BookForm()
    d = {'EBFO': EBFO}
    return render(request, 'insert_book.html', d)