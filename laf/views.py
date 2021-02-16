from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemRegister,ItemFound
from .models import User,Founder
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    img= User.objects.all()
    if request.method=="POST":
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']
        subject = request.POST['subject']
        send_mail(
            email,
            message,
            email,
            ['suradkarsantosh1@gmail.com'],
            fail_silently=False,

        )
    return render(request,'index.html',{'img':img})

def report(request):
    if request.method == 'POST':
        fm = ItemRegister(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = ItemRegister()
    form = ItemRegister()
    img= User.objects.all()
    return render(request, 'report.html',{'img':img,'form':fm})

def found(request):
    if request.method == 'POST':
        fm = ItemFound(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = ItemFound()
    form = ItemFound()
    img= Founder.objects.all()
    return render(request, 'found.html',{'img':img,'form':fm})

def view(request, myid):
    img= User.objects.filter(id=myid)
    return render(request, 'view.html',{'img':img[0]})



     
