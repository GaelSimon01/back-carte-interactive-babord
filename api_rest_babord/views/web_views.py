from django.shortcuts import render
from django.http import HttpResponse
from api_rest_babord.models import *
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "api_rest_babord/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
@method_decorator(login_required, name='dispatch')
class ConcertListView(ListView):
    model = Concert
    template_name = "api_rest_babord/list_concert.html"
    context_object_name = "concerts"
    
    def get_queryset(self):
        user = self.request.user
        return Concert.objects.filter(groupe__utilisateur__user=user)
    

class ConnectView(LoginView):
    template_name = 'api_rest_babord/login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'api_rest_babord/home.html',{'titreh1':"hello "+username+", you're connected"})
        else:
            return render(request, 'api_rest_babord/register.html')
   
class RegisterView(TemplateView):
    template_name = 'api_rest_babord/register.html'
    
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'api_rest_babord/login.html')
        else:
            return render(request, 'api_rest_babord/register.html')


class DisconnectView(TemplateView):
    template_name = 'api_rest_babord/logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)