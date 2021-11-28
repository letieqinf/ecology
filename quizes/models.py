from django.db import models
import random

# Create your models here.

DIFF_CHOICES = (
    ('начальный', 'easy'), 
    ('средний', 'medium'), 
    ('продвинутый', 'hard')
)

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField()
    difficulty = models.CharField(max_length=11,choices=DIFF_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.topic}'

    def get_questions(self):
        questions = list(self.question_set.all())
        if self.imagequestion_set.all():
            questions = list(self.imagequestion_set.all())

        random.shuffle(questions)

        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'