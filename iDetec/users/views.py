from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def home(request):
    return render(request, 'index.html')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    users = User.objects.all()
    return render(request, 'CRUD/listUser.html', {
        'users': users
    })


def detail(request, id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    user = User.objects.get(pk=id)
    # profil
    return render(request, 'profile.html', {
        'user': user
    })


def edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    id1 = id
    if request.method == "GET":
        user = User.objects.filter(id=id).get
        return render(request, 'CRUD/editUser.html', {
            'user': user
        })
    else:
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        user = User(id1, nom, prenom, username, email, password, role)
        user.save()

        return redirect('/users')


def delete(request, id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    user = User.objects.get(pk=id).delete()

    return redirect('/users')


def create(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    if request.method == "GET":
        return render(request, 'CRUD/createUser.html')
    else:
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        role = request.POST['role']

        if password == cpassword:
            user = User(None, nom, prenom, username, email, password, role)
            user.save()

            return redirect('/users')
        else :
            messages.success(request, "Your passWord dont match !")
            return render(request, 'CRUD/createUser.html', {})





def upload(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    if request.method == "POST":
        if len(request.FILES) != 0:
            image = request.FILES['img']

        ap = Images(None, image)
        ap.save()

        return redirect('list-ano')
    else:
        return render(request, 'upload.html')

def addAnom(request,id):
    image = Images.objects.filter(id=id).get
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    if request.method == "GET":

        return render(request,'anomalie.html',{
            'image': image
        })
    else:

        nom = request.POST['name']
        desc = request.POST['desc']
        type = request.POST['type']
        pts = request.POST['pts']

        ano = Anomaly(None,nom,desc,type,id)
        ano.save()

        id_ano = ano.id
        points = pts.split("-")

        for p in points:
            point = p.split(";")
            x = point[0]
            y = point[1]
            px = Pixel(None,x,y,id_ano)
            px.save()

        return redirect('list-ano')


def listAnom(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    images = Images.objects.all();

    return render(request,'listAno.html',{
        'images' : images
    })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.success(request,"Your passWord or username is not correct !")
            return render(request,'registration/login.html',{})
    else:
        return render(request,'registration/login.html',{})

def logout_user(request):
    logout(request)
    return redirect('login')

def listanno(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    anomaly = Anomaly.objects.all()

    return render(request, 'listanomali.html', {
        'anomaly': anomaly
    })

def showAno(request,id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {})
    anomaly = Anomaly.objects.filter(id=id).get
    pixels = Pixel.objects.filter(anomaly_id=id)

    return render(request, 'showAno.html', {
        'anomaly': anomaly,
        'pixels': pixels
    })