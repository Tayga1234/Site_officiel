from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    
    #Services
    path('service', views.service, name='service'),
    path('service/<int:offre_id>', views.detail_offre, name='detail_offre'),
    
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('subscribe', views.subscribe, name='subscribe'),
]
