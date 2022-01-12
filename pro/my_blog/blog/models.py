from django.db import models

class Enfant(models.Model):
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
    sexe = models.CharField('Sexe', max_length=20)
    nomp = models.CharField('NomP', max_length=120)
    fonctionp = models.CharField('FonctionP', max_length=120)
    situationM = models.CharField('situation matrimoniale', max_length=120)
    nomm = models.CharField('NomM', max_length=120)
    fonctionm = models.CharField('FonctionM', max_length=120)
    situationM = models.CharField('situation matrimoniale', max_length=120)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom