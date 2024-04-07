from rest_framework import serializers
from .models import Book

#serializei os campos do book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'date', 'author', 'genre', 'publisher']
