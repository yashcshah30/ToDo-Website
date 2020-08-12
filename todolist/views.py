from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ReminderForm
from .models import ToDo
import datetime

def home(request):
	
	today_is_empty = False
	upcoming_is_empty = False

	yesterday_posts = ToDo.objects.filter(due_date__lt=datetime.datetime.now().date())
	if len(yesterday_posts)!=0:
		yesterday_posts.delete()

	if request.method=='POST':
		form = ReminderForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your list reminder has been submitted!')
			return redirect('to-do')
	else:	
		form = ReminderForm()	

	if len(ToDo.objects.all())==0:
		is_empty = True
	else: 
		is_empty = False

	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	today_posts = ToDo.objects.filter(due_date__range=(today_min, today_max)).all()

	if len(today_posts)==0:
		today_is_empty = True

	upcoming_posts = ToDo.objects.filter(due_date__gt=datetime.datetime.now().date()).order_by("due_date")

	if len(upcoming_posts)==0:
		upcoming_is_empty = True

	return render(request, "todolist/home.html", {'form':form, 'today_posts':today_posts, 'upcoming_posts':upcoming_posts, 'is_empty':is_empty, 'today_is_empty':today_is_empty, 'upcoming_is_empty':upcoming_is_empty})


def remove(request, par1):
	del_post = ToDo.objects.filter(id=par1).first()
	del_post.delete()
	messages.info(request, f'Your reminder has been deleted')
	return redirect('to-do')

def update(request, par2):
	post = ToDo.objects.get(pk=par2)
	if request.method=='POST':
		u_form = ReminderForm(request.POST, instance = post)
		if(u_form.is_valid()):
			u_form.save()
			messages.success(request, f'Your reminder has been updated!')
			return redirect('to-do')
	else:
		u_form = ReminderForm(instance = post)

	return render(request, "todolist/update.html", {'u_form' : u_form})
