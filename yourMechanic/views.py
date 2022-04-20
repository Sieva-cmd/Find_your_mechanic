from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from yourMechanic.forms import LoginForm, SignupForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignupForm()
    
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_mechanic:
                login(request, user)
                return redirect('mechanic')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def mechanic(request):
    return render(request,'mechanic.html')

def home(request):
    return render(request,'home.html')
