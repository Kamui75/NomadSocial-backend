from django.db import models

class Useraccount(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.TextField()
