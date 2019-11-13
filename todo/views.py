from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoList, Category
from datetime import datetime, timedelta
from django.utils import timezone

def index(request):
	todos = TodoList.objects.all()
	categories = Category.objects.all()
	if request.method == "POST":

		if "taskAdd" in request.POST:
			title = request.POST["description"]
			date = str(request.POST["date"])
			category = request.POST["category_select"]
			if category == '':
				category = Category.objects.last()
			if date == '':
				date = timezone.now()+timedelta(days=3)
			content = title
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save()
			return redirect("/")

		if "taskDelete" in request.POST:
			checkedlist = request.POST["checkedbox"]
			todo = TodoList.objects.get(id=int(checkedlist))
			todo.delete()
	return render(request, "index.html", {"todos": todos, "categories":categories})
	
def todoView(request):
	return HttpResponse('Hello my friend')
# Create your views here.
