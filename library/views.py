from django.http import JsonResponse
from django.http import HttpResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import requests

#aqui implemento o GET geral e o POST

@api_view(['GET', 'POST'])
def book_list(request, format=None):

    if request.method == 'GET':
        library = Book.objects.all()
        serializer = BookSerializer(library, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


'''
Exemplos para POST
    {
        "title": "O Pequeno Principe",
        "date": "1943-06-04",
        "author": "Antoine de Saint-Exupéry",
        "genre": "Fabula",
        "publisher": "HarperCollins Brasil"
    },
    {
        "title": "Diario de um Banana",
        "date": "2007-01-04",
        "author": "Jeff Kinney",
        "genre": "Humor",
        "publisher": "New York Times"
    }
'''


#aqui implemento o GET especifico, o PUT e o DELETE

@api_view(['GET', 'PUT', 'DELETE']) 
def book_detail(request, id, format=None):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#nao implementei a HOME, mas aviso para ir para endpoints validos

def home(request):

    return HttpResponse("HOME nao implemenetada Acesse: /library,   /library/<id>,   /booklist")


#aqui dou o render para o html do /booklist

def booklist(request):
    # Faz uma solicitação à sua própria API Django para recuperar os dados
    response = requests.get('http://127.0.0.1:8000/library/')
    data = response.json()  # Converte a resposta em formato JSON em um dicionário Python

    # Passa os dados recuperados para o template HTML
#    print(data)  # Verifica se os dados estão corretos
    return render(request, 'library/library.html', {'library': data})
