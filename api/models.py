# api/models.py
from django.db import models

class UserProfile(models.Model):
    firebase_uid = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Enqueteur(models.Model):
    class Enqueteur(models.Model):
        firebase_id = models.CharField(max_length=128, unique=True)  # Firebase User ID
        nom = models.CharField(max_length=100)
        email = models.EmailField(unique=True)

        def __str__(self):
            return self.nom
    email = models.EmailField(unique=True)
    localisation = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Enquete(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    enqueteur = models.ForeignKey(Enqueteur, on_delete=models.CASCADE, related_name='enquetes')

    def __str__(self):
        return self.titre
