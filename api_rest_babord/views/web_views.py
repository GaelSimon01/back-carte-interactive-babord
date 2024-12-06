from django.shortcuts import render, redirect
from django.http import HttpResponse
from api_rest_babord.models import *
from api_rest_babord.forms import *
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.utils.decorators import method_decorator

####################### Page diverse #######################

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "api_rest_babord/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        user = self.request.user

        concerts = Concert.objects.filter(groupe__utilisateur__user=user)
        print(concerts)
        if(concerts.count() > 0):
            context['concerts'] = concerts[:7]

        albums = Album.objects.filter(groupe__utilisateur__user=user)
        if(albums.count() > 0):
            context['albums'] = albums[:7]
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
####################### Concert #######################

@method_decorator(login_required, name='dispatch')
class ConcertListView(ListView):
    model = Concert
    template_name = "api_rest_babord/basicViews/list_concert.html"
    context_object_name = "concerts"
    
    def get_queryset(self):
        user = self.request.user
        concert_valider = Concert.objects.filter(groupe__utilisateur__user=user, valider=True)
        concerts_en_attente = Concert.objects.filter(groupe__utilisateur__user=user, valider=False)
        queryset = {
            'concert_valider': concert_valider,
            'concerts_en_attente': concerts_en_attente
        }
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titre'] = "Détail du concert"
        return context

@method_decorator(login_required, name='dispatch')
class ConcertDetailView(DetailView):
    model = Concert
    template_name = "api_rest_babord/basicViews/detail_concert.html"
    context_object_name = "concert"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titre'] = "Détail du concert"
        return context

@login_required
def consert_create(request):
    if request.method == 'POST':
        form = ConcertForm(request.POST)
        if form.is_valid():
            intitule = form.cleaned_data['intitule']
            date_debut = form.cleaned_data['date_debut']
            lieu = form.cleaned_data['lieu']
            groupe = request.user.utilisateur.groupe
            concert = Concert.objects.create(intitule=intitule, date_debut=date_debut, lieu=lieu, groupe=groupe)
            concert.save()
            return redirect('concerts-list')
    else:
        form = ConcertForm()
    return render(request, 'api_rest_babord/actionsViews/new_object.html', {'form': form, 'titre_create': 'Créer un concert'})

@login_required
def concert_update(request, pk):
    concert = Concert.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConcertForm(request.POST, instance=concert)
        if form.is_valid():
            form.save()
            return redirect('concerts-list')
    else:
        form = ConcertForm(instance=concert)
    return render(request, 'api_rest_babord/actionsViews/update_object.html', {'form': form, 'titre_update': 'Modifier un concert'})

@login_required
def concert_delete(request, pk):
    concert = Concert.objects.get(pk=pk)

    if request.method == "POST":
        concert.delete()
        return redirect('concerts-list')

    context = {
        'subject': "concert",
        'titre_delete': "Vous vous apprêtez à supprimer un concert,\n êtes-vous sûr ?",
    }
    return render(request, 'api_rest_babord/actionsViews/delete_object.html', context)

####################### ALBUMS #######################

@method_decorator(login_required, name='dispatch')
class AlbumListView(ListView):
    model = Album
    template_name = "api_rest_babord/basicViews/list_album.html"
    context_object_name = "albums"
    
    def get_queryset(self):
        user = self.request.user
        album_valider = Album.objects.filter(groupe__utilisateur__user=user, valider=True)
        albums_en_attente = Album.objects.filter(groupe__utilisateur__user=user, valider=False)
        queryset = {
            'album_valider': album_valider,
            'albums_en_attente': albums_en_attente
        }
        return queryset
    
@method_decorator(login_required, name='dispatch')
class AlbumDetailView(DetailView):
    model = Album
    template_name = "api_rest_babord/basicViews/detail_album.html"
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titre'] = "Détail de l'album"
        return context
    
@login_required
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            libelle = form.cleaned_data['libelle']
            description = form.cleaned_data['description']
            date_sortie = form.cleaned_data['date_sortie']
            lieu = None
            groupe = request.user.utilisateur.groupe
            album = Album.objects.create(libelle=libelle, description=description, date_sortie=date_sortie, lieu=lieu, groupe=groupe)
            album.save()
            return redirect('albums-list')
    else:
        form = AlbumForm()
    return render(request, 'api_rest_babord/actionsViews/new_object.html', {'form': form, 'titre_create': 'Créer un album'})

@login_required
def album_update(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('albums-list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'api_rest_babord/actionsViews/update_object.html', {'form': form, 'titre_update': 'Modifier un album'})

@login_required
def album_delete(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == "POST":
        album.delete()
        return redirect('albums-list')

    context = {
        'subject': "album",
        'titre_delete': "Vous vous apprêtez à supprimer un album,\n êtes-vous sûr ?",
    }
    return render(request, 'api_rest_babord/actionsViews/delete_object.html', context)
################### Authentification ###################

class ConnectView(LoginView):
    template_name = 'api_rest_babord/login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'api_rest_babord/register.html')
   
class RegisterView(TemplateView):
    template_name = 'api_rest_babord/register.html'

    def usernameVerif(self, username):
        try:
            user = User.objects.get(username=username)
            return True
        except User.DoesNotExist:
            return False
    
    def emailVerif(self, email):
        try:
            user = User.objects.get(email=email)
            return True
        except User.DoesNotExist:
            return False
        
    def groupeVerif(self, groupe_name):
        try:
            groupe = Groupe.objects.get(libelle=groupe_name)
            return True
        except Groupe.DoesNotExist:
            return False
        
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)

        validEmail = self.emailVerif(mail)
        validUsername = self.usernameVerif(username)
        validGroupe = self.groupeVerif(request.POST.get('group_name', False))
        
        if validEmail or validUsername or validGroupe:
            return render(request, 'api_rest_babord/register.html',{
                'error': [
                    {'email': validEmail},
                    {'username': validUsername},
                    {'group_name': validGroupe}
                ]
            })
        
        user = User.objects.create_user(username, mail, password)
        libelle = request.POST.get('group_name', False)
        groupe = Groupe.objects.create(libelle=libelle)

        utilisateur = Utilisateur.objects.create(user=user, groupe=groupe)

        user.save()
        utilisateur.save()
        groupe.save()

        if user is not None and user.is_active:
            return render(request, 'api_rest_babord/login.html')
        else:
            return render(request, 'api_rest_babord/register.html')


class DisconnectView(TemplateView):
    template_name = 'api_rest_babord/logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)