from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def task(request):
    return render(request, 'home/get_task.html')


def create_task(request):
    if request.method=='POST':
        task = request.POST['task']
        note = request.POST['note'] 
        new_task = Todo(task=task, note=note, mark=False)
        new_task.save()

        messages.success(request, "New Task created.")
        return render(request, 'home/index.html')
    else:
        messages.success(request, "Task was not created.")
        return redirect('/')


def view_task(request):
    task = Todo.objects.all()
    context = {
        'task':task,
    }
   
    return render(request, 'home/mark_complete.html', context) 


def mark_complete(request):
    task = Todo.objects.all()
    
    #Generating a list of all the task ids
    id_all=[]
    for t in task:
        id_all.append(t.id)
    # print(id_all)

    if request.method=='POST':
        list=request.POST.getlist('mark')
        #Converting the list of ids (type=string) into type=int
        id_list=[]
        for id in list:
            id_list.append(int(id))

        for id in id_all:
            if id in id_list:
                Todo.objects.filter(pk=id).update(mark=True)
            else:
                Todo.objects.filter(pk=id).update(mark=False)
        # print(id_list)
    
    return redirect('/mark_complete')

def delete_update(request):
    task = Todo.objects.all()
    context = {
        'task':task,
    }
    return render(request, 'home/delete_update.html', context)


def delete_task(request, id):
    if id:
        task=Todo.objects.get(pk=id)
        task.delete()
    return redirect('/delete_update')


def update_task(request, id):
    if id:
        task = Todo.objects.get(pk=id)
        context = {
            'task':task,
        }
    return render(request, 'home/update_task.html', context)


def save_updated_task(request, id):
    if request.method=='POST':
        task = request.POST['task']
        note = request.POST['note']

        t = Todo.objects.get(pk=id)
        t.task = task
        t.note = note
        t.save()
        return redirect('/delete_update')






