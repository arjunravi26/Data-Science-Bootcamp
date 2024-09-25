from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'user':'Arjun'})
def personal(request):
    return render(request,'personal.html')