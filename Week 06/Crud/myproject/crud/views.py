from crud.models import User
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    if request.POST:
        name = request.POST.get('name')
        age = request.POST.get('age')
        if name and age:
            print(name,age)
            user = User.objects.create(name=name,age=age)
            user.save()
    return render(request,'index.html')
    
def display(request):
    users = User.objects.all()
    return render(request,'display.html',{'users':users})

def delete(request):
    ids = request.GET.get('id')
    user = User.objects.get(id=ids)
    user.delete()
    return redirect('display')