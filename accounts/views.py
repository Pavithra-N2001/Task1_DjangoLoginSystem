from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .form import DoctorSignupForm,PatientSignupForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
       return render(request,'register.html')

class doctor_register(CreateView):
    model=User
    form_class= DoctorSignupForm
    template_name='doctor_register.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index/')

class patient_register(CreateView):
    model=User
    form_class= PatientSignupForm
    template_name='patient_register.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def index_view(request):
    return render(request,'index.html')

