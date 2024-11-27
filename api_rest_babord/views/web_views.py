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
        return Concert.objects.filter(groupe__utilisateur__user=user)

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
            lieu = None
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
        user = User.objects.create_user(username, mail, password)

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