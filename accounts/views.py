from django.contrib.messages.api import success
from django.shortcuts import redirect, render

from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.http.response import JsonResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView

from .forms import UserRegistrationForm

from django.core import serializers

import json

from quizes.models import Quiz
from results.models import Result


class Login(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Данные некорректны')

        ctx = {}
        return render(request, self.template_name, ctx)

@method_decorator(login_required, name='dispatch')
class LogOut(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('index')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class Register(TemplateView):
    form = UserRegistrationForm()

    template_name = 'register.html'

    def get(self, request):
        ctx = {'form': self.form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {user} успешно создан')

            return redirect('login')

        error_list = []
        if form.errors:
            for errors in form.errors:
                for error in form.errors[errors]:
                    error_list.append(error)

        ctx = {'form': self.form, 'errors':error_list}
        return render(request, self.template_name, ctx)

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = 'profile.html'
    def get(self, request):
        quiz_tuple = Quiz.objects.values_list('name', 'topic', 'number_of_questions', 'pk')
        results_tuple = Result.objects.values_list('quiz', 'user', 'score')

        quiz_json = serializers.serialize('json', Quiz.objects.all())
        quiz = json.loads(quiz_json)

        results_json = serializers.serialize('json', Result.objects.all())
        results = json.loads(results_json)

        ctx = {'quiz':quiz, 'quiz_tuple':quiz_tuple, 'results':results, 'results_tuple':results_tuple}
        return render(request, self.template_name, ctx)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
