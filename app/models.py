from django.db import models
from django.conf import settings


class Author(models.Model):
    name = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, unique=True
    )

    def __str__(self):
        return self.name.username


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='author')
    contributors = models.ManyToManyField(Author,  blank=True)

    def __str__(self):
        return self.name

    @property
    def contributors_list(self):
        return [con.name for con in self.contributors.all()]


class Section(models.Model):
    name = models.CharField(max_length=40)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    p_sec = models.ForeignKey('Section', null=True,
                              blank=True, on_delete=models.CASCADE)
    sub_sec = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # for auto checking the sub_sec field
    def save(self, *args, **kwargs):
        if self.p_sec is not None:
            self.sub_sec = True
        return super(Section, self).save(*args, **kwargs)
