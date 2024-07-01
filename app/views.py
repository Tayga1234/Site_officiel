from django.shortcuts import get_object_or_404, render
from .models import *
# Rendre le code moins long en creant une fonction qui pourrait prendre touts les objets en parametres concernant l'affichage
# Create your views here.

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Subscription

import logging

# Configurer le logger
logger = logging.getLogger(__name__)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        next_page = request.POST.get('next')
        if email:
            try:
                # Vérifier si l'email existe déjà dans la base de données
                if not Subscription.objects.filter(email=email).exists():
                    # Enregistrer l'email dans la base de données
                    Subscription.objects.create(email=email)
                    messages.success(request, 'Vous etes desormais un abonné!')

                    # Envoyer un email de confirmation
                    send_mail(
                        'Mail de confirmation',
                        'Bonjour très cher nouvel abonné! Nous sommes heureux de vous compter parmi nous.',
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                else:
                    messages.info(request, 'Cet email est déjà abonné.')
            except Exception as e:
                # Log l'erreur et afficher un message d'erreur
                logger.error(f"Error during subscription: {e}")
                messages.error(request, "Une erreur s'est produite lors de l'enregistrement")

        else:
            messages.error(request, 'Please enter a valid email address.')

        # Rediriger vers la page d'origine ou la page d'accueil par défaut
        return redirect(next_page or '/')
    return redirect('/')

def home(request):
    
    headers = Header.objects.first()
    accueil = Accueil.objects.first()
    presentations = Presentation.objects.all()
    valeurs = Valeur.objects.all()
    carasteristique1s = Carasteristique1.objects.all()
    carasteristique2 = Carasteristique2.objects.first()
    carasteristique3s = Carasteristique3.objects.all()
    questions = Question.objects.all()
    temoins = Temoin.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, 'Merci pour votre abonnement !')
            else:
                messages.error(request, 'Cet email est déjà abonné.')
            
        else:
            messages.error(request, 'Veuillez entrer une adresse e-mail valide.')
            
    context={
        'headers': headers,
        'accueil': accueil,
        'presentations':presentations,
        'valeurs':valeurs,
        'carasteristique1s':carasteristique1s,
        'carasteristique2':carasteristique2,
        'carasteristique3s':carasteristique3s,
        'questions':questions,
        'temoins':temoins,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        'section':section,
        
    }
    return render(request, 'home.html',context)

def about(request):
    headers = Header.objects.first()
    abouts = About.objects.first()
    domaines = Domaine.objects.all()
    outils = OutilsLangage.objects.all()
    blogs = Blog.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()

    context={
        'headers': headers,
        'abouts':abouts,
        'domaines':domaines,
        'outils':outils,
        'blogs':blogs,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
    }
    
    return render(request, 'about.html',context)

#-------------------------------------------------
    #----------------SERVICES---------------------
#-------------------------------------------------
def service(request):
    headers = Header.objects.first()
    services = Service.objects.first()
    offres = Offre.objects.all()
    postes = Poste.objects.all()
    projets = Projet.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()
    teams = Team.objects.first()
    outils = OutilsLangage.objects.all()
    partenaires= Partenaire.objects.all()

    context={
        'headers': headers,
        'services': services,
        'offres':offres,
        'postes':postes,
        'projets':projets,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'infos':infos,
        'section':section,
        'teams': teams,
        'outils': outils,
        'partenaires':partenaires,
        
    }
    return render(request, 'service.html',context)

def detail_offre(request, offre_id):
    offre = get_object_or_404(Offre, pk=offre_id)
    
    headers = Header.objects.first()
    services = Service.objects.first()
    offres = Offre.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()
    m1 = Methode1.objects.first()
    m2 = Methode2.objects.first()
    m3 = Methode3.objects.first()
    cadres = Cadre.objects.all()
    outils = OutilsLangage.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()
    teams = Team.objects.first()
    postes = PosteMembre.objects.all()
    context={
        'headers': headers,
        'teams': teams,
        'postes':postes,
        'm1':m1,
        'm2':m2,
        'm3':m3,
        'cadres': cadres,
        'outils': outils,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        'section':section,
        'offre':offre,
        'services':services,
    }
    return render(request, 'services/detail.html', context)

def team(request):
    headers = Header.objects.first()
    teams = Team.objects.first()
    postes = PosteMembre.objects.all()
    m1 = Methode1.objects.first()
    m2 = Methode2.objects.first()
    m3 = Methode3.objects.first()
    cadres = Cadre.objects.all()
    outils = OutilsLangage.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()
    section = Section.objects.first()

    context={
        'headers': headers,
        'teams': teams,
        'postes':postes,
        'm1':m1,
        'm2':m2,
        'm3':m3,
        'cadres': cadres,
        'outils': outils,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        'section':section,
        
    }
    return render(request, 'team.html',context)

def contact(request):
    headers = Header.objects.first()
    contacts= Contact.objects.first()
    cards = Card.objects.all()
    socials = Social.objects.all()
    footers = Footer.objects.first()
    liens = Lien.objects.all()
    offres = Offre.objects.all()
    infos = Info.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            try:
                # Enregistrement du message dans la base de données
                ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
                
                # Envoi de l'email
                send_mail(
                    subject,
                    f"Message from {name} ({email}):\n\n{message}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Votre message a été envoyé. Merci!')
            except Exception as e:
                messages.error(request, f"Une erreur s'est produite : {e}")
        else:
            messages.error(request, 'Tous les champs sont obligatoires.')
  # Redirige vers la page de contact après le traitement

    context={
        'headers': headers,
        'contacts':contacts,
        'cards':cards,
        'socials':socials,
        'footers':footers,
        'liens':liens,
        'offres':offres,
        'infos':infos,
        
    }
    return render(request, 'contact.html',context)

def blog(request):
    return render(request, 'blog.html')
