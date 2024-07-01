from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Header)
admin.site.register(Footer)
admin.site.register(Social)
admin.site.register(Lien)
admin.site.register(Accueil)
admin.site.register(Presentation)
admin.site.register(Valeur)
admin.site.register(Carasteristique1)
admin.site.register(Carasteristique2)
admin.site.register(Carasteristique3)
admin.site.register(Question)
admin.site.register(Temoin)
admin.site.register(Info)
admin.site.register(Section)


admin.site.register(About)
admin.site.register(Domaine)
admin.site.register(OutilsLangage)
admin.site.register(Blog)

admin.site.register(Service)
admin.site.register(Offre)
admin.site.register(Poste)
admin.site.register(Projet)
admin.site.register(Partenaire)
admin.site.register(Team)
admin.site.register(PosteMembre)
admin.site.register(Methode1)
admin.site.register(Methode2)
admin.site.register(Methode3)
admin.site.register(Cadre)

admin.site.register(Contact)
admin.site.register(Card)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')

admin.site.register(ContactMessage)