
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .models import MyUser
from Movies.models import Movies, movieCertificate, movieLanguage, movieShowtime, movieType
from Movies.forms import AddMovieForm, AddMovieCertificate, AddMovieType, AddMovieLanguage, AddMovieShowtime




def dashboard(request):
    UserCount = MyUser.objects.all().count()
    movieCount = Movies.objects.all().count()
    userRec = {
        'UserCount':UserCount,
        'movieCount':movieCount
    }
    
    return render(request,'accounts/dashboard.html',userRec)

def UserRecord(request):
    UserData = MyUser.objects.all()
    
    userRec={
        'UserData':UserData,
        
    }
    return render(request,'accounts/UserRecord.html',userRec)

def addUser(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "User Added Successfully!")
        return redirect("UserRecord")
    else:
        print("Not saved")
    
    return render(request,'accounts/addUser.html',{'form':form})

def viewUser(request, id=None):
    rec=MyUser.objects.get(pk=id)
    

    return render(request,'accounts/viewUser.html',{'rec':rec})

def deleteUser(request, id=None):
    if request.method == "POST":
        print("yes")
        rec=MyUser.objects.get(pk=id)
        rec.delete()
        data = {
            'rec':rec
        }
        return redirect("UserRecord")
    return render(request,'accounts/deleteUser.html',data)
        
def movieDetails(request,id=None):
    movieData = Movies.objects.get(pk=id)
    movieRec = {
        'movieData':movieData
    }
    
    return render(request,'Movies/movieDetails.html',movieRec)

def viewTrailer(request,id=None):
    movieData = Movies.objects.get(pk=id)
    movieRec = {
        'movieData':movieData
    }
    
    return render(request,'Movies/viewTrailer.html',movieRec)
        

   
   
    
    

    
    
def movieRecord(request):
    movieData = Movies.objects.all()
    movieRec = {
        'movieData':movieData
    }
    return render(request,'Movies/movieRecord.html',movieRec)

def addMovie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print("Not saved")
    else:
        form = AddMovieForm()
        
    return render(request,'Movies/addMovie.html',{'form':form})

def movieCertificateRecord(request):
    certificateData = movieCertificate.objects.all()
    certificateRec = {
        'certificateData':certificateData
    }
    return render(request, 'Movies/movieCertificateRecord.html',certificateRec)

def addMovieCertificate(request):
    if request.method == 'POST':
        form = AddMovieCertificate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieCertificateRecord")
        else:
            print("Not Saved")
    else:
        form = AddMovieCertificate()
    return render(request,'Movies/addMovieCertificate.html',{'form':form})

def movieTypeRecord(request):
    categoryData = movieType.objects.all()
    categoryRec = {
        'categoryData':categoryData
    }
    return render(request, 'Movies/movieTypeRecord.html',categoryRec)

def addMovieType(request):
    if request.method=="POST":
        form = AddMovieType(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieTypeRecord")
    else:
        form = AddMovieType()
    return render(request,'Movies/addMovieType.html',{'form':form})

def movieLanguageRecord(request):
    languageData = movieLanguage.objects.all()
    languageRec = {
        'languageData':languageData
    }
    return render(request, 'Movies/movieLanguageRecord.html',languageRec)



def addMovieLanguage(request):
    if request.method=="POST":
        form = AddMovieLanguage(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieLanguageRecord")
    else:
        form = AddMovieLanguage()
    return render(request,'Movies/addMovieLanguage.html',{'form':form})

def movieShowtimeRecord(request):
    showtimeData = movieShowtime.objects.all()
    showtimeRec = {
        'showtimeData':showtimeData
    }
    return render(request, 'Movies/movieShowtimeRecord.html',showtimeRec)

def addMovieShowtime(request):
    if request.method=="POST":
        form = AddMovieShowtime(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieShowtimeRecord")
    else:
        form = AddMovieShowtime()
    return render(request,'Movies/addMovieShowtime.html',{'form':form})

def seatView(request):
    return render(request,'Movies/seatView.html')

    
# Create your views here.
def home(request):
    first_name = ""
    userId = request.session.get('userId', None)
    if userId is not None:
        user = MyUser.objects.get(id=userId)
        first_name = user.first_name
    movieData = Movies.objects.all()
    data = {
        "first_name": first_name,
        'movieData': movieData
    }
    return render(request, "accounts/index.html",data)


@csrf_exempt
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created.")
            return redirect('signin')
        else:
            messages.error(request,"Invalids Informations")
    return render(request, "accounts/register.html",{'form':form})

def signin(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'] 
            )
            print(user)


            if user:
                login (request,user,backend='django.contrib.auth.backends.ModelBackend')
                userId= MyUser.objects.get(email=form.cleaned_data['email']).id
                request.session['userId'] = userId
                user = MyUser.objects.get(id=userId)
                movieData = Movies.objects.all()
                data = {
                    "first_name": user.first_name,
                    "user":user,
                    'movieData': movieData
                }
                return render(request, 'accounts/index.html', data)
            else:
                print("Bad credentials.")
    form = LoginForm() 

    return render(request, "accounts/login.html",{'form':form})

def signout(request):
    logout(request)
    messages.success(request, "Logout successfully!!")
    return redirect('home')
    
def adminDashboard(request):
    userId = request.session.get('userId', None)
    if userId is not None:
        user = MyUser.objects.get(id=userId)
        if user.is_superuser:
            return render(request, 'accounts/dashboard.html')
        else:
            return HttpResponse("Access Denied!!")
    else:
        return HttpResponse("Access Denied!!")
    
    