from django.shortcuts import render

from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.http.response import JsonResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Map(TemplateView):
    template_name = 'map.html'
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)