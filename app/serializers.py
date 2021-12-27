# Local Import
from django.utils.functional import empty
from rest_framework import serializers
from .models import (Book, Author, Section)
# 3rd party imports
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    sections = serializers.SerializerMethodField()  # custom method

    # getting the book related sections
    def get_sections(self, obj):
        sections = obj.section_set.filter(p_sec__isnull=True).values('name')
        # checking if book sections exists
        if sections.exists():
            return sections
        return []

    class Meta:
        model = Book
        fields = ['name', 'sections', 'author', 'contributors']


class SectionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ['book', 'name', 'p_sec']

    def create(self, validate_data):
        crnt_user = self.context['user']  # request user
        book_author = validate_data['book'].author.name
        allwd_prnt_sec = validate_data['book'].section_set.all()

        # checking for the the author contributer
        if book_author.id is crnt_user.id or crnt_user in [i.name for i in validate_data['book'].contributors.all()]:
            # Adding try block to catch the parent section if not exist
            try:
                if validate_data['p_sec'] in allwd_prnt_sec:
                    sec = Section.objects.create(**validate_data)
                    return sec
            except:
                sec = Section.objects.create(**validate_data)
                return sec
            raise serializers.ValidationError(
                'This sections belongs to another book')

        raise serializers.ValidationError(
            "You are neither  the author nor contributor ")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
