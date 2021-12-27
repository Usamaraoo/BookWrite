from django.shortcuts import render, HttpResponse
# local imports
from app.models import (Book, Author, Section)
from app.serializers import (
    BookSerializer, SectionSerializers, AuthorSerializer)

# 3rd party imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class IndexApi(APIView):
    def get(self, request):
        return Response({
            'Books': 'http://127.0.0.1:8000/api/books/',
            'sections': 'http://127.0.0.1:8000/api/sections/',
            'authors': 'http://127.0.0.1:8000/api/authors/'
        })


class BookAPi(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        ser = BookSerializer(books, many=True)
        return Response(ser.data)


class SectionApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        sections = Section.objects.all()
        ser = SectionSerializers(sections, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        user = Token.objects.get(key=request.auth.key).user
        ser = SectionSerializers(data=request.data, context={'user': user})

        if ser.is_valid():
            ('this is the user', ser)
            ser.save()
            return Response(ser.data)

        return Response(ser.errors)


class AuthorApi(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        ser = AuthorSerializer(authors, many=True)
        return Response(ser.data)
