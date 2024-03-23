
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout 
from django.contrib import messages
from .forms import add_record_form
from .models import record

def home(request):
	records=record.objects.all()

	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)

		if user:
			login(request,user)
			messages.success(request,'STATUS : You have been Logged in ')
			return redirect('home')
		else:
			messages.success(request,'STATUS : Somethign is wrong ')
			return redirect('home')
	return render(request,'home.html',{'records':records})


def logout_user(request):
	logout(request)
	messages.success(request,'STATUS : Successfully Logged out ')
	return redirect('home')

def add_task(request):
	form =add_record_form(request.POST or None)
	if request.user.is_authenticated:
		if request.method=='POST':
			if form.is_valid():
				add_record=form.save()
				messages.success(request,'STATUS : Record added Successfully')
				return redirect('home')
		return render(request,'add_task.html',{'form':form})
	else:
		messages.success(request,'STATUS : Please Login...')
		return redirect('home')


def done_task(request,pk):
	if request.user.is_authenticated:
		that_task=record.objects.get(id=pk)
		that_task.status='DONE'
		that_task.save()
		messages.success(request,'STATUS : Task Number '+str(that_task.id)+" Done")
	return redirect('home')

def undo_task(request,pk):
	that_task=record.objects.get(id=pk)
	that_task.status='TODO'
	that_task.save()
	messages.success(request,'STATUS : Task Number '+str(that_task.id)+" Undone")
	return redirect('home')

def task_done(request):
	if request.user.is_authenticated:
		objects=record.objects.all()
		return render(request,'done_task.html',{'records':objects})
	else:
		return redirect('home')

def task_not_done(request):
	if request.user.is_authenticated:
		objects=record.objects.all()
		return render(request,'not_done_task.html',{'records':objects})
	return redirect('home')

def remove_task(request,pk):
	if request.user.is_authenticated:
		this_task=record.objects.get(id=pk)
		this_task.delete()
		messages.success(request,'STATUS : Task Number '+str(pk)+" Removed")
	return redirect('home')

def edit_task(request,pk):
	if request.user.is_authenticated:
		this_task=record.objects.get(id=pk)
		this_form=add_record_form(request.POST or None, instance=this_task)
		if this_form.is_valid():
			this_form.save()
			return redirect('home')
		return render(request,'edit_task.html',{'form':this_form})
	return redirect('home')
