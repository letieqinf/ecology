from django.shortcuts import render

from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.http.response import JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView

@method_decorator(login_required, name='dispatch')
class List(TemplateView):
    template_name = 'list.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Mac(TemplateView):
    template_name = 'mac.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')   
class Metal(TemplateView):
    template_name = 'met.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Glass(TemplateView):
    template_name = 'glass.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Plastic(TemplateView):
    template_name = 'plastic.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Box(TemplateView):
    template_name = 'box.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Wastes(TemplateView):
    template_name = 'dangerous_wastes.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Clothes(TemplateView):
    template_name = 'clothes.html'
    
    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
