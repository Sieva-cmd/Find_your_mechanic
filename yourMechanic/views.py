from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from yourMechanic.forms import LoginForm, SignupForm
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  FullBodyPaint, StereoSetup,EngineRepair,Customer,Mechanic
from .serializer import FullBodyPaintSerializer,StereoSetupSerializer,EngineRepairSerializer,CustomerSerializer,MechanicSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly



from .models import User


from .serializers import UserSerializer, RegisterSerializer

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





class RegisterList(APIView):
    def get(self, request, format=None):
        all_user = User.objects.all()
        serializers = RegisterSerializer(all_user, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)







class FullBodyPaintList(APIView):
    def get(self, request, format=None):
        paint = FullBodyPaint.objects.all()
        serializers = FullBodyPaintSerializer(paint, many=True)
        return Response(serializers.data)

        
    def post(self, request, format=None):
        serializers = FullBodyPaintSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class StereoSetupList(APIView):
    def get(self, request, format=None):
        stereo = StereoSetup.objects.all()
        serializers = StereoSetupSerializer(stereo, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = StereoSetupSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class EngineRepairList(APIView):
    def get(self, request, format=None):
        engine = EngineRepair.objects.all()
        serializers = EngineRepairSerializer(engine, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = EngineRepairSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class CustomerList(APIView):
    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializers = CustomerSerializer(customer, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class MechanicList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        mechanic = Mechanic.objects.all()
        serializers = MechanicSerializer(mechanic, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = MechanicSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

