from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoList, Category
from datetime import datetime, timedelta
from django.utils import timezone
import requests
from django.core.files import File
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required

def index(request):
	todos = TodoList.objects.filter(polzovatel=request.user)
	categories = Category.objects.all()
	
	return render(request, "index.html", {"todos": todos, "categories": categories})

def adding(request):
	if request.method == "POST":

		if "taskAdd" in request.POST:
			title = request.POST["description"]
			date = str(request.POST["date"])
			category = request.POST["category_select"]
			photo = request.POST["image"]

			if category == '':
				category = Category.objects.last()
			if date == '':
				date = timezone.now()+timedelta(days=3)
			content = title

			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category), picture=photo)
			
			if request.user.is_authenticated:
				Todo.polzovatel = request.user
			Todo.save()
		return render(request)			

def deleting(request):

		if "taskDelete" in request.POST:
			
			checkedlist = request.POST["checkedbox"]
			todo = TodoList.objects.get(id=int(checkedlist))
			todo.delete()
		
		return render(request)

def contact(request):
	return render(request, 'todo/contact.html')

class all(generic.ListView):
	model=TodoList

class det(generic.DetailView):
	model=TodoList
# Create your views here.
