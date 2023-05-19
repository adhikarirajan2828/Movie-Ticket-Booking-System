from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, RegisterForm, OtpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .models import MyUser, otp
from Movies.models import Ticket

import barcode
from barcode.writer import ImageWriter
from barcode import EAN13

from io import BytesIO
from django.template.loader import get_template

from xhtml2pdf import pisa

from Movies.models import (
    Movies,
    movieCertificate,
    movieLanguage,
    movieShowtime,
    movieType,
    movieStatus
 )
from Movies.forms import (
     AddMovieForm,
     AddMovieCertificate,
     AddMovieType,
     AddMovieLanguage,
     AddMovieShowtime,
     movieForm
 )
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

import random

from django.http import HttpResponse


def dashboard(request):
    print('helrjlk')
    UserCount = MyUser.objects.all().count()
    movieCount = Movies.objects.all().count()
    userRec = {"UserCount": UserCount, "movieCount": movieCount}
    print(UserCount)

    return render(request, "accounts/dashboard.html", userRec)


def UserRecord(request):
    UserData = MyUser.objects.all()

    userRec = {
        "UserData": UserData,
    }
    return render(request, "accounts/UserRecord.html", userRec)


def addUser(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "User Added Successfully!")
        return redirect("UserRecord")
    else:
        print("Not saved")

    return render(request, "accounts/addUser.html", {"form": form})


def viewUser(request, id=None):
    rec = MyUser.objects.get(pk=id)

    return render(request, "accounts/viewUser.html", {"rec": rec})

#@login_required(login_url="signin")
@csrf_exempt
def deleteUser(request, id):
    print(id)
    user = get_object_or_404(MyUser, pk=id)
    print("Deleting user-------------------")
    print(user)
    print(request.method)
    if request.method == "POST":
        user.delete()
        messages.success(request,"User Deleted Successfully")
        print('good')
        return redirect("/UserRecord")
    return HttpResponse('method not allowed')

@login_required(login_url="signin")
def movieDetails(request, id=None):
    movieData = Movies.objects.get(pk=id)
    request.session["movieId"] = id
    print("movie ID ",request.session["movieId"])
    request.session["movie_title"] = movieData.movie_title
    print(request.session["movie_title"])
    print( movieData.movie_showtime.all())
    movieRec = {"movieData": movieData, "showtime": movieData.movie_showtime.all()}

    return render(request, "Movies/movieDetails.html", movieRec)

@csrf_exempt
def deleteCategory(request, id=None):
    category = movieType.objects.get(id=id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted successfully")
        return redirect("movieTypeRecord")
    return HttpResponse("Method not allowed!")


@csrf_exempt
def deleteLanguage(request, id=None):
    language = movieLanguage.objects.get(id=id)
    if request.method == "POST":
        language.delete()
        messages.success(request, "language deleted successfully")
        return redirect("movieLanguageRecord")
    return HttpResponse("Method not allowed!")

@csrf_exempt
def deleteMovie(request, id=None):
    movie = Movies.objects.get(id=id)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Movie deleted successfully")
        return redirect("movieRecord")
    return HttpResponse("Method not allowed!")




def addMovieStatus(request):
    if request.method == "POST":
        form = addMovieStatus(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieCertificateRecord")
        else:
            print("Not Saved")
    else:
        form = addMovieStatus()
    return render(request, "Movies/movieStatus.html", {"form": form})


def viewTrailer(request, id=None):
    movieData = Movies.objects.get(pk=id)
    movieRec = {"movieData": movieData}

    return render(request, "Movies/viewTrailer.html", movieRec)


def movieRecord(request):
    movieData = Movies.objects.all()
    movieRec = {"movieData": movieData}
    return render(request, "Movies/movieRecord.html", movieRec)


def editMovieRecord(request, id=None):
    movie = get_object_or_404(Movies, id=id)
    form = movieForm(request.POST or None, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("movieRecord")
    return render(request, "Movies/editMovieRecord.html", {"form": form})

def addMovie(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie_title = form.cleaned_data['movie_title']
            movie_exists = Movies.objects.filter(movie_title=movie_title).exists()
            if movie_exists:
                messages.info(request, "Title already exists!")
                return render(request, "Movies/addMovie.html", {"form": form})
            
            form.save()
            return redirect("home")
    else:
        form = AddMovieForm()

    return render(request, "Movies/addMovie.html", {"form": form})


def movieCertificateRecord(request):
    certificateData = movieCertificate.objects.all()
    certificateRec = {"certificateData": certificateData}
    return render(request, "Movies/movieCertificateRecord.html", certificateRec)

@csrf_exempt
def deleteCertificate(request, id=None):
    certificate = movieCertificate.objects.get(id=id)
    if request.method == "POST":
        certificate.delete()
        redirect("movieCertificateRecord")
    return HttpResponse("Invalid request")

def addMovieCertificate(request):
    if request.method == "POST":
        form = AddMovieCertificate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieCertificateRecord")
        else:
            print("Not Saved")
    else:
        form = AddMovieCertificate()
    return render(request, "Movies/addMovieCertificate.html", {"form": form})


def movieTypeRecord(request):
    categoryData = movieType.objects.all()
    categoryRec = {"categoryData": categoryData}
    return render(request, "Movies/movieTypeRecord.html", categoryRec)


def addMovieType(request):
    if request.method == "POST":
        form = AddMovieType(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieTypeRecord")
    else:
        form = AddMovieType()
    return render(request, "Movies/addMovieType.html", {"form": form})


def movieLanguageRecord(request):
    languageData = movieLanguage.objects.all()
    languageRec = {"languageData": languageData}
    return render(request, "Movies/movieLanguageRecord.html", languageRec)


def addMovieLanguage(request):
    if request.method == "POST":
        form = AddMovieLanguage(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieLanguageRecord")
    else:
        form = AddMovieLanguage()
    return render(request, "Movies/addMovieLanguage.html", {"form": form})


def movieShowtimeRecord(request):
    showtimeData = movieShowtime.objects.all()
    showtimeRec = {"showtimeData": showtimeData}
    return render(request, "Movies/movieShowtimeRecord.html", showtimeRec)

@csrf_exempt
def deleteShowTime(request, id=None):
    showTime = movieShowtime.objects.get(id=id)
    if request.method == "POST":
        showTime.delete()
        redirect("movieShowtimeRecord")
    return HttpResponse("Invalid request")

def addMovieShowtime(request):
    if request.method == "POST":
        form = AddMovieShowtime(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movieShowtimeRecord")
    else:
        form = AddMovieShowtime()
    return render(request, "Movies/addMovieShowtime.html", {"form": form})


# Create your views here.
def home(request):
    img_slider = Movies.objects.all()
    first_name = ""
    uid = request.session.get("userId", None)
    if uid is not None:
        first_name = MyUser.objects.get(id=uid).first_name
    
    running = movieStatus.objects.get(id=1) #running
    upcoming = movieStatus.objects.get(id=2) #upcoming
    upcomingMovies = Movies.objects.filter(movie_status=upcoming)
    runningMovies = Movies.objects.filter(movie_status=running)   
    data = {"first_name": first_name, "upcomingMovies": upcomingMovies, "runningMovies": runningMovies,"img_slider":img_slider}
    return render(request, "accounts/index.html", data)


def otpView(request):
    form = OtpForm()
    return render(request, "accounts/otp.html", {"form": form})


def verifyOTP(otp_value, id):
    print(
        "verifying otp value................................................................"
    )
    print(otp_value, id)
    user = MyUser.objects.get(id=id)
    querySet = otp.objects.filter(email=user.email, otp=otp_value).last()
    if querySet is not None:
        return True
    return False


def verifyOTPView(request):
    form = OtpForm()
    print(request.method)
    if request.method == "POST":
        form = OtpForm(request.POST)
        if form.is_valid():
            otpValue = form.cleaned_data["otp"]
            print("otp", otpValue)
            userId = request.session["userId"]
            print("userID", userId)
            user = MyUser.objects.get(id=userId)

            verify = verifyOTP(otpValue, userId)
            if verify:
                return redirect("signin")
            else:
                messages.error(request, "Invalid OTP")
                msg = messages.get_messages(request)

    return render(request, "accounts/otp.html", {"form": form})


def sendOTP(recepient):
    try:
        otp_value = random.randint(100000, 999999)
        print("OTP from sendOTP function ", otp_value)
        subject = "verify email"
        message = f"Your OTP is {otp_value}"
        from_email = settings.EMAIL_HOST_USER

        send_mail(
            subject,
            message,
            from_email,
            [
                recepient,
            ],
            fail_silently=False,
        )
        otp.objects.create(otp=otp_value, email=recepient)
    except Exception as e:
        print(e)
    return


@csrf_exempt
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created.")
            email = form.cleaned_data["email"]
            request.session["userId"] = MyUser.objects.get(email=email).id
            sendOTP(email)
            return redirect("otp")
        else:
            messages.error(request, "Password must be of 8 characters. It must conatin 1 number, 1 uppercase, 1 lowercase, 1 letter. It must not contain firstname and lastname")
    return render(request, "accounts/register.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"], password=form.cleaned_data["password"]
            )
            print(user)

            if user:
                login(
                    request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
                user = MyUser.objects.get(email=form.cleaned_data["email"])
                request.session["userId"] = user.id
                movieData = Movies.objects.all()
                data = {
                    "first_name": user.first_name,
                    "user": user,
                    "movieData": movieData,
                }
                return render(request, "accounts/index.html", data)
            else:
                print("Bad Credentials")
        else:
            messages.error(request,"Invalid Informations")
    form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def signout(request):
    logout(request)
    messages.success(request, "Logout successfully!!")
    return redirect("home")


@login_required(login_url="signin")
def adminDashboard(request):
    userId = request.session.get("userId", None)
    if userId is not None:
        UserCount = MyUser.objects.all().count()
        ticketCount = Ticket.objects.all().count()
        movieCount = Movies.objects.all().count()
        userRec = {"UserCount": UserCount, "movieCount": movieCount,"ticketCount": ticketCount}
        user = MyUser.objects.get(id=userId)
        if user.is_superuser:
            return render(request, "accounts/dashboard.html",userRec)
        else:
            return HttpResponse("Access Denied!!")
    else:
        return HttpResponse("Access Denied!!")


@login_required(login_url="signin")
def rewardPoint(request):
    if request.method == "GET":
        userId = request.session["userId"]
        user = MyUser.objects.get(id=userId)
        context = {"points": user.reward_point}
        print(f"context--- {context}")
        return render(request, "Movies/myLoyalty.html", context)
    return HttpResponse("Invalid Request!!")


def generate_barcode(tickets):
    for ticket in tickets:
        barcode_digits = str(ticket.ticket_id + 1000000000000)
        print(barcode_digits)
        barcode_format = barcode.get_barcode_class("code39")
        my_barcode = barcode_format(barcode_digits, writer=ImageWriter())
        # img = EAN13(str(barcode_digits), writer=ImageWriter())
        filename = f"{ticket.ticket_id}"
        # img.save(f"static/img/barcodes/{filename}")
        my_barcode.save(f"static/img/barcodes/{filename}")


@login_required(login_url="signin")
def myTickets(request):
    if request.method == "GET":
        try:
            userId = request.session["userId"]
            print(userId)
            ticketInfo = Ticket.objects.filter(user=MyUser.objects.get(id=userId))
            print(ticketInfo)
            if not ticketInfo:
                return HttpResponse("The tickets you buy will show here")
            context = {"ticketInfo": ticketInfo}
            print(context)
            generate_barcode(ticketInfo)
            return render(request, "Movies/myTickets.html", context)
        except Exception as e:
            print(e)
            return HttpResponse(f"Internal server error")
    return HttpResponse("Invalid Method")



def render_to_pdf(template_src, context_dict={}):
    result = BytesIO()
    template = get_template(template_src)
    html  = template.render(context_dict)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
    


@login_required(login_url="signin")
def tickets(request):
    if request.method == "GET":
        try:
            userId = request.session["userId"]
            print(userId)
            ticketInfo = Ticket.objects.filter(user=MyUser.objects.get(id=userId))
            context = {"tickets": ticketInfo}
            pdf = render_to_pdf('Movies/tickets.html', context)
            print(context)
            return HttpResponse(pdf, content_type='application/pdf')
        except Exception as e:
            print(e)
            return HttpResponse(f"Internal server error")
    return HttpResponse("Invalid Method")
