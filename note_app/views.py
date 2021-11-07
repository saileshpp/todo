from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from note_app.models import todo

# Create your views here.
def home(request):
    
    if request.method == 'GET':
        items = todo.objects.all()[0:3]
        return render(request, 'index.html',{'items' : items})
    else:
        title = request.POST["title"]
        note = request.POST["note"]

        value = todo.objects.create(title = title, note = note)
        value.save()

        return redirect('home')


def note_view(request):
    items = todo.objects.all()
    return render(request, 'note-view.html', {'items': items})

def edit(request, id):
    to_do = todo.objects.get(id=id)
    
    if request.method == 'GET':   
        return render(request, 'edit.html', {'todo':to_do})
    
    else:
        to_do.title = request.POST['title']
        to_do.note = request.POST['note']
        to_do.save()
        return redirect('home')

def delete(request, id):
    to_do = todo.objects.get(id=id)
    to_do.delete()

    return redirect('home')
    
def view(request, id):
    item = todo.objects.get(id=id)

    return render(request, 'view.html', {'item':item})
