from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from .models import book,publishing_house
from .forms import bookform

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import bookserializer,publishing_houseserializer


# Create your views here.


def all_book(request):
    books = book.objects.all()
    context={
        'books':books
    }
    return render(request, 'books/books.html', context)

def show_details(request,id):
    books = book.objects.get(id=id)
    context={
        'books':books
    }
    return render(request, 'books/book_details.html', context)

# def aa(request):
#     return HttpResponse("book_lab")


def add_book(request):
    book_form = bookform()
    context = {}
    try:
        if request.method == 'POST':
            book_form = bookform(request.POST, request.FILES)
            if book_form.is_valid():
                book_form.save()
                return redirect('all_book')

        else:
            book_form = bookform()
        context = {
            'book_form': book_form,
            'title': 'add_book'
        }
    except Exception as e:
        print(f'error in add_book => {e}')
    return render(request, 'books/add_book.html', context)

def edit_book(request,id):
    book_form = bookform()
    context = {}
    try:
        editbook= book.objects.get(id=id)
        if request.method == 'POST':
            book_form = bookform(request.POST or None,request.FILES or None, instance=editbook)
            if book_form.is_valid():
                book_form.save()
                return redirect('all_book')
        
        else : 
            book_form = bookform(instance=editbook)
        context = {
            "book_form": book_form,
            "title": 'Edit Book'
        }
    except Exception as e:
        print(f'error in edit_book => {e}')
    return render(request, 'books/add_book.html', context)



def delete_book(request,id):
    try:
        deletebook = book.objects.get(id=id)
        deletebook.delete()
    except Exception as e:
        print(f'error in delete_student => {e}')
    return redirect('all_book')
    


# _________________api_view____________________

@api_view(['GET'])
def all_book_api(request):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        books = book.objects.all()
        book_serializer = bookserializer(books, many=True).data
        data['books'] = book_serializer
        req_status = status.HTTP_200_OK
    except Exception as e:
        print(f'error in all_book_api => {e}')
    return Response(data=data, status=req_status)

@api_view(['POST'])
def add_book_api(request):
    req_status = status.HTTP_400_BAD_REQUEST
    data={}
    try:
        new_book = bookserializer(data=request.data)
        if new_book.is_valid():
            new_book.save()
            data['book'] = new_book.data
            req_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f'error in all_book_api => {e}')
    return Response(data=data, status=req_status)

# -------------------------------
# put, patch
@api_view(['PUT'])
def edit_book_api(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        books = get_object_or_404(book, id=id)
        x = bookserializer(instance=books, data=request.data, partial=True)
        if x.is_valid():
            x.save()
            req_status = status.HTTP_200_OK
            data['books'] = x.data
    except Exception as e:
        print(f'error in edit_book_api => {e}')
    return Response(data=data, status=req_status)

# delete
@api_view(['DELETE'])
def delete_book_api(request, id):
    req_status = status.HTTP_400_BAD_REQUEST
    data = {}
    try:
        books = get_object_or_404(book, id=id)
        book_serializer = bookserializer(instance=books).data
        books.delete()
        req_status = status.HTTP_204_NO_CONTENT
        data['books'] = book_serializer
    except Exception as e:
        print(f'error in delete_book_api => {e}')
    return Response(data=data, status=req_status)

