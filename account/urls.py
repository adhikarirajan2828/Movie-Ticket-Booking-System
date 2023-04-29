from django.contrib import admin
from django.urls import path, include
from . import views

# from account.views import HomeView, AddMovieView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    # path('',HomeView.as_view(),name="home"),
    # path('add_movie/',AddMovieView.as_view(), name='add-movie'),
    # path('movies/<int:pk>',MovieDetailView.as_view(),name='movies-details'),
    path("movieRecord", views.movieRecord, name="movieRecord"),
    path("addMovie", views.addMovie, name="addMovie"),
    path("addMovieCertificate", views.addMovieCertificate, name="addMovieCertificate"),
    path(
        "movieCertificateRecord",
        views.movieCertificateRecord,
        name="movieCertificateRecord",
    ),
    path("addMovieType", views.addMovieType, name="addMovieType"),
    path("movieTypeRecord", views.movieTypeRecord, name="movieTypeRecord"),
    path("addMovieLanguage", views.addMovieLanguage, name="addMovieLanguage"),
    path("movieLanguageRecord", views.movieLanguageRecord, name="movieLanguageRecord"),
    path("addMovieShowtime", views.addMovieShowtime, name="addMovieShowtime"),
    path("movieShowtimeRecord", views.movieShowtimeRecord, name="movieShowtimeRecord"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("dashboard", views.adminDashboard, name="dashbaord"),
    path("UserRecord", views.UserRecord, name="UserRecord"),
    path("addUser", views.addUser, name="addUser"),
    path("viewUser<id>", views.viewUser, name="viewUser"),
    path("deleteUser<id>", views.deleteUser, name="deleteUser"),
    path("movieDetails<id>", views.movieDetails, name="movieDetails"),
    path("viewTrailer<id>", views.viewTrailer, name="viewTrailer"),
    path("seatView", views.seatView, name="seatView"),
    path("sendotp", views.sendOTP, name="sendOTP"),
    path("mytickets", views.myTickets,name="mytickets"),
    path("myloyalty", views.rewardPoint, name='rewardpoints'),
    path("otp", views.otpView, name='otp'),
    path("verifyotp", views.verifyOTPView, name='verify-otp')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
