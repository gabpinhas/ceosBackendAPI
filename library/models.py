from django.db import models

#Crio meu modelo Book, com os atributos title, date, author, genre e publisher
class Book(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)

    def __str__(self):
        return self.title + ' ' + self.author