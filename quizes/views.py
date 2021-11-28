from json.encoder import JSONEncoder
from django.contrib.messages.api import success
from django.shortcuts import redirect, render

from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.http.response import JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Quiz
from questions.models import ImageQuestion, Question, ImageAnswer, Answer
from results.models import Result

# Create your views here.

class QuizList(ListView):
    model = Quiz
    template_name = 'quizes.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz.html', {'quiz':quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        images = []
        for i in q.get_images():
            images.append(i)

        questions.append({str(q):{'answers':answers, 'images':images}})
    return JsonResponse({
        'data': questions
    })

def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        is_image = False

        desc = []
        for k in data_.keys():
            while ('null' in data_[k]):
                data_[k].remove('null')

            try:
                question = Question.objects.get(text=k)
            except Exception:
                is_image = True
                question = ImageQuestion.objects.get(text=k)
            questions.append(question)
            try:
                desc.append(question.description)
            except Exception:
                pass
        
        q_dict = {}
        for q in questions:
            q_dict[q.text] = []
            answers = ...

            if is_image:
                answers = ImageAnswer.objects.filter(question=q)
            else:
                answers = Answer.objects.filter(question=q)
            
            for a in answers:
                if a.correct:
                    q_dict[q.text].append(a.text)

        score = 0
        results = {'correct':q_dict, 'desc':desc, 'is_correct':[]}

        for ch in q_dict:
            q_tmp = sorted(q_dict[ch])
            data_tmp = sorted(data_[ch])
            if q_tmp == data_tmp:
                score += 1
                results['is_correct'].append(True)
            else:
                results['is_correct'].append(False)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        results['score'] = score

        try:
            user_result = Result.objects.get(quiz=quiz, user=user)

            if user_result.score < score:
                results['score'] -= user_result.score
                user_result.score = score
                user_result.save()
            else:
                results['score'] = 0
        except Exception:
            Result.objects.create(quiz=quiz, user=user, score=score)

    return JsonResponse({'data':results})