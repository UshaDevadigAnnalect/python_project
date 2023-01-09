from django.shortcuts import render
from quiz.models import Quiz
import random

def qpage(request):
	questions = Quiz.objects.all()[:10]
	questions = list(questions)
	random.shuffle(questions)

	return render(request, 'quiz.html', { 'questions': questions})
	
	
