from django.shortcuts import render,redirect,HttpResponse
from . models import signup,gallery
from . forms import RegisterForm,LoginForm,EditForm,GalleryForm
# Create your views here.
def Sign(request):
    return render(request,'Signin_up.html')

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    else:
        form = RegisterForm()
        return render(request, 'Register.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('/home/')
    else:
        form = LoginForm()
        return render(request, 'Login.html', {'form1': form})


def Home(request):
    return render(request,'Home.html',)

def delete_user(request,id):
    delete_user = signup.objects.filter(Userid = id).delete()
    return redirect('/home/')

def edit(request, id):
    user = signup.objects.get(Userid = id)
    print(user)
    form = EditForm(instance = user)
    if request.method == 'POST':
        form = EditForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    else:
        form = EditForm(instance= user)
        return render(request, 'Edit.html',{'form':form})


def Gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/home/')
    else:
        form = GalleryForm()
        return render(request, 'Gallery.html', {'form': form})


def View(request):
    user = signup.objects.all()
    return render(request,'View.html',{'users':user})