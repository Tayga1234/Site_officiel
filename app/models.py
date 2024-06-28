from django.db import models

# Create your models here.
class Section(models.Model):
    image_home = models.ImageField(upload_to='media/section/')
    image_service = models.ImageField(upload_to='media/section/')
    image_footer = models.ImageField(upload_to='media/section/')
    image_equipe = models.ImageField(upload_to='media/section/')

class Header(models.Model):
    logo = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)#nom entreprise
    onglet_1 = models.CharField(max_length=200)#home
    onglet_2 = models.CharField(max_length=200)#about
    onglet_3 = models.CharField(max_length=200)#service
    onglet_4 = models.CharField(max_length=200)#team
    onglet_5 = models.CharField(max_length=200)#contact

class Footer(models.Model):
    text_abonne = models.CharField(max_length=200)#home
    sous_text_abonne = models.CharField(max_length=200)#home
    button_abonne = models.CharField(max_length=200)#
    name_urbain = models.CharField(max_length=200)#
    text = models.CharField(max_length=200)#
    lien = models.CharField(max_length=200)#
    service = models.CharField(max_length=200)#
    contact = models.CharField(max_length=200)#
    crypt = models.CharField(max_length=200)#
    design = models.CharField(max_length=200)#

class Social(models.Model):
    name = models.CharField(max_length=200)#
    lien = models.CharField(max_length=200)# 
    icon = models.CharField(max_length=200)#

class Lien(models.Model):
    lien = models.CharField(max_length=200)#
    url = models.CharField(max_length=200)#

class Info(models.Model):
    lieu1 = models.CharField(max_length=200)#
    lieu2 = models.CharField(max_length=200)#
    lieu3 = models.CharField(max_length=200)#
    contact = models.CharField(max_length=200)#
    contact2 = models.CharField(max_length=200, blank=True, null=True)#
    email = models.CharField(max_length=200)#
    email2 = models.CharField(max_length=200, blank=True, null=True)#


class Accueil(models.Model):
    slogan = models.CharField(max_length=200)
    sous_slogan = models.CharField(max_length=200)
    Bouton_page1 = models.CharField(max_length=200)#home
    image_1_accueil = models.ImageField(upload_to='media/acceuil/')

    text_presentation = models.CharField(max_length=200)#titre pour presentation
    sous_text_presentation = models.CharField(max_length=200)#text d'accroche

    text_valeur = models.CharField(max_length=200)#titre pour valeur
    sous_text_valeur = models.CharField(max_length=200)#text d'accroche

    text_carasteristique = models.CharField(max_length=200)#titre pour presentation
    sous_text_carasteristique1 = models.CharField(max_length=200)#text d'accroche
    image1 = models.ImageField(upload_to='media/carasteristique/')
    sous_text_carasteristique2 = models.CharField(max_length=200)#text d'accroche
    image2 = models.ImageField(upload_to='media/carasteristique/')
    sous_text_carasteristique3 = models.CharField(max_length=200)#text d'accroche
    image3 = models.ImageField(upload_to='media/carasteristique/')

    title_carasteristique2_1 = models.CharField(max_length=200)
    title_carasteristique2_2 = models.CharField(max_length=200)
    title_carasteristique2_3 = models.CharField(max_length=200)

    text_question = models.CharField(max_length=200)#titre pour question
    sous_text_question = models.CharField(max_length=200)#text d'accroche
    
    text_temstimonail = models.CharField(max_length=200)#titre pour temoignage
    sous_text_testimonail = models.CharField(max_length=200)#text d'accroche


class Presentation(models.Model):
    image = models.ImageField(upload_to='media/presentation/')
    title_presentation = models.CharField(max_length=200)
    text_presentation = models.CharField(max_length=200)

class Valeur(models.Model):
    image = models.ImageField(upload_to='media/valeur/')
    title_valeur = models.CharField(max_length=200)
    text_valeur = models.CharField(max_length=200)


class Carasteristique1(models.Model):
    text_domaine = models.CharField(max_length=200)

class Carasteristique2(models.Model):
    title1 = models.CharField(max_length=200)
    sout_text1 = models.TextField(max_length=500)
    sous_titre1_1  = models.CharField(max_length=200)
    sous_text1_1 = models.TextField(max_length=500)
    sous_titre1_2 = models.CharField(max_length=200)
    sous_text1_2 = models.TextField(max_length=500)
    sous_titre1_3 = models.CharField(max_length=200)
    sous_text1_3 = models.TextField(max_length=500)

    title2 = models.CharField(max_length=200)
    sout_text2 = models.TextField(max_length=500)
    sous_titre2_1 = models.CharField(max_length=200)
    sous_text2_1 = models.TextField(max_length=500)
    sous_titre2_2 = models.CharField(max_length=200)
    sous_text2_2 = models.TextField(max_length=500)
    sous_titre2_3 = models.CharField(max_length=200)
    sous_text2_3 = models.TextField(max_length=500)

    title3 = models.CharField(max_length=200)
    sout_text3 = models.TextField(max_length=500)
    sous_titre3_1 = models.CharField(max_length=200)
    sous_text3_1 = models.TextField(max_length=500)
    sous_titre3_2 = models.CharField(max_length=200)
    sous_text3_2 = models.TextField(max_length=500)
    sous_titre3_3 = models.CharField(max_length=200)
    sous_text3_3 = models.TextField(max_length=500)

class Carasteristique3(models.Model):
    icon = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    text = models.TextField(max_length=500)

class Question(models.Model):
    titre = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    js2 = models.TextField(max_length=500)

class Temoin(models.Model):
    person_name = models.CharField(max_length=200)
    person_poste = models.CharField(max_length=200)
    text = models.TextField(max_length=500)


# Pour l'onglet a propos
class About(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)

    image1 = models.ImageField(upload_to='media/about/')
    image2 = models.ImageField(upload_to='media/about/')
    image3 = models.ImageField(upload_to='media/about/')

    title_resume = models.CharField(max_length=200)
    text_resume = models.TextField()

    Name_Urbain = models.CharField(max_length=200)
    Email_Urbain = models.CharField(max_length=200)
    Horaire = models.CharField(max_length=200)

    text_domain = models.CharField(max_length=200)#titre pour domaine
    sous_text_domaine = models.CharField(max_length=200)#text d'accroche
    sous_text_domaine2 = models.CharField(max_length=200)#text d'accroche
    sous_text_domaine3 = models.CharField(max_length=200)#text d'accroche
    sous_text_domaine4 = models.CharField(max_length=200)#text d'accroche    

    text_partenaire = models.CharField(max_length=200)#titre pour partenaire
    sous_text_partenaire = models.CharField(max_length=200)#text d'accroche

    text_blog = models.CharField(max_length=200)#titre pour partenaire
    sous_text_blog = models.CharField(max_length=200)#text d'accroche

class Domaine(models.Model):
    domaine = models.CharField(max_length=200)

class OutilsLangage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/outils/')

class Partenaire(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/partenaires/')

class Blog(models.Model):
    image = models.ImageField(upload_to='media/blog/')
    date = models.CharField(max_length=200)
    text = models.CharField(max_length=200)#text d'accroche
    

#Pour l'onglet Services

class Service(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)

    text_service = models.CharField(max_length=200)#titre pour service
    sous_text_service = models.CharField(max_length=200)#text d'accroche
    image = models.ImageField(upload_to='media/service/')

    text_equipe = models.CharField(max_length=200)#titre pour equipe
    sous_text_equipe = models.CharField(max_length=200)#text d'accroche
    sous_text_equipe1 = models.CharField(max_length=200)#text d'accroche
    sous_text_equipe2 = models.CharField(max_length=200)#text d'accroche

    text_part = models.CharField(max_length=200)#titre pour partenaire
    sous_text_part = models.CharField(max_length=200)#text d'accroche

    text_projet = models.CharField(max_length=200)#titre pour partenaire
    sous_text_projet = models.CharField(max_length=200)#text d'accroche

class Offre(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)#text d'accroche
    color = models.CharField(max_length=100)

class Poste(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)#text d'accroche

class Projet(models.Model):
    image = models.ImageField(upload_to='media/projets/')
    title = models.CharField(max_length=200)
    display = models.CharField(max_length=100)
    js1 = models.CharField(max_length=100)
    js2 = models.CharField(max_length=100)


class Team(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)

    text_team = models.CharField(max_length=200)#titre pour service
    sous_text_team = models.CharField(max_length=200)#text d'accroche

    text_meth = models.CharField(max_length=200)#titre pour equipe
    sous_text_meth = models.CharField(max_length=200)#text d'accroche
   
    text_cadre = models.CharField(max_length=200)#titre pour partenaire
    sous_text_cadre = models.CharField(max_length=200)#text d'accroche
 
    text_outil = models.CharField(max_length=200)#titre pour partenaire
    sous_text_outil = models.CharField(max_length=200)#text d'accroche

class PosteMembre(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)#text d'accroche
    display = models.CharField(max_length=10)

class Methode1(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    
    meth_1 = models.CharField(max_length=200)#titre pour methode
    text_meth_1 = models.CharField(max_length=200)#text d'accroche

    meth_2 = models.CharField(max_length=200)#titre pour methode
    text_meth_2 = models.CharField(max_length=200)#text d'accroche

    meth_3 = models.CharField(max_length=200)#titre pour methode
    text_meth_3 = models.CharField(max_length=200)#text d'accroche

    image = models.ImageField(upload_to='media/team/')

class Methode2(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    
    meth_1 = models.CharField(max_length=200)#titre pour methode
    text_meth_1 = models.CharField(max_length=200)#text d'accroche

    meth_2 = models.CharField(max_length=200)#titre pour methode
    text_meth_2 = models.CharField(max_length=200)#text d'accroche

    meth_3 = models.CharField(max_length=200)#titre pour methode
    text_meth_3 = models.CharField(max_length=200)#text d'accroche

    image = models.ImageField(upload_to='media/team/')

class Methode3(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    
    meth_1 = models.CharField(max_length=200)#titre pour methode
    text_meth_1 = models.CharField(max_length=200)#text d'accroche

    meth_2 = models.CharField(max_length=200)#titre pour methode
    text_meth_2 = models.CharField(max_length=200)#text d'accroche

    meth_3 = models.CharField(max_length=200)#titre pour methode
    text_meth_3 = models.CharField(max_length=200)#text d'accroche

    image = models.ImageField(upload_to='media/team/')

class Cadre(models.Model):
    image = models.ImageField(upload_to='media/team/cadre/')
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    text = models.CharField(max_length=200)#text d'accroche
    display = models.CharField(max_length=10)


class Contact(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)

    text_contact = models.CharField(max_length=200)#titre pour 
    map_localisation = models.CharField(max_length=500)

class Card(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text1 = models.CharField(max_length=200)#text d'accroche
    text2 = models.CharField(max_length=200, blank=True, null=True)

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"