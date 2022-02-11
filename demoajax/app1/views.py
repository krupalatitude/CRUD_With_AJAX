from django.shortcuts import render, redirect
from .models import UserDetail


def IndexView(request):
    if request.method == 'POST':
        model = UserDetail()
        model.full_name = request.POST['full_name']
        model.email_id = request.POST['email_id']
        model.password = request.POST['password']
        model.save()
        return redirect('index')
    else:
        data = UserDetail.objects.all()
        context = {
            'data' : data
        }
    return render(request, 'index.html', context)

def EditView(request, id):
    data = UserDetail.objects.get(id = id)
    if request.method=='POST':
        data.full_name = request.POST['full_name']
        data.email_id = request.POST['email_id']
        data.password = request.POST['password']
        data.save()  
        return redirect('index')  
    context = {
        'data' : data
    }
    return render(request, 'edit.html', context)

def DeleteView(request, id):
    data = UserDetail.objects.get(id = id)
    data.delete()
    return redirect('index')