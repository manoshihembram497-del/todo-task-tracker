from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from taskapi.models import Task

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
               messages.info(request, "Email is already in use!")
               return redirect('register')
            elif User.objects.filter(username=username).exists():
               messages.info(request, "Username is already in use!")
               return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not the same!")
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User= auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, User)
            return redirect('dashboard')
        else:
            messages.info(request, "Credentials Invalid!")
            return redirect('login')
    return render(request, 'login.html')

def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    search_query = request.GET.get('search')
    if search_query:
     tasks = Task.objects.filter(title__icontains = search_query)
    else:
        tasks = Task.objects.all()

    return render(request, 'dashboard.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']

        Task.objects.create(
            user = request.user,
            title = title,
            description = description,
            due_date = due_date
        )
        return redirect('dashboard')
    return render(request, 'add_task.html')

def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']

        task.save()
        return redirect('dashboard')
    return render(request, 'edit_task.html', {'task' : task})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('dashboard')

def completed_task(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard')
