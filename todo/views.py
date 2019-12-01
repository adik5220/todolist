from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoList, Category
from datetime import datetime, timedelta
from django.utils import timezone
import requests
from django.core.files import File
from django.views import generic

def index(request):
	todos = TodoList.objects.all()
	categories = Category.objects.all()
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
			Todo.save()
			return redirect("/todo/")

		if "taskDelete" in request.POST:
			
			checkedlist = request.POST["checkedbox"]
			todo = TodoList.objects.get(id=int(checkedlist))
			todo.delete()
	return render(request, "index.html", {"todos": todos, "categories":categories})
	


class all(generic.ListView):
	model=TodoList

class det(generic.DetailView):
	model=TodoList
# Create your views here.
