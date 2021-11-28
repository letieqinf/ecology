from django.db import models
from quizes.models import Quiz

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()

    def get_images(self):
        return []

class ImageQuestion(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    first_image = models.CharField(max_length=200)
    second_image = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.imageanswer_set.all()

    def get_images(self):
        return [self.first_image, self.second_image]

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'question: {self.question.text}, answer: {self.text}, correct: {self.correct}'

class ImageAnswer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(ImageQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'question: {self.question.text}, answer: {self.text}, correct: {self.correct}'