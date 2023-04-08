from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Ticket
import json


@csrf_exempt
def seatView(request):
    return render(request, "Movies/seatView.html")


@login_required(login_url="signin")
@csrf_exempt
def book_ticket(request):
    if request.method == "POST":
        print("Booking Ticket")
        data = json.loads(request.body)
        print(data)
        Ticket.objects.create(
            movie_title=request.session["movie_title"],
            seat_number=" ".join(map(str, data["seatSelectedNumber"])),
            price=data["totalPrice"],
            # total_selected_seats=data["totalSeatCount"],
            movie_date=request.session["movie_date"],
        )
        print("ticket created successfully")
        return HttpResponse(status=200)  # redirect('seatView')
    return HttpResponse("<h3>Something went wrong!</h3>")


@login_required(login_url="signin")
@csrf_exempt
def ticket_date(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            date = data["date"]
            print("-----------backend---------")
            print(date)
            request.session["movie_date"] = date
            movie_title = request.session["movie_title"]  # movie_date = date
            print(movie_title)  # |
            query_set = Ticket.objects.filter(
                movie_title=movie_title, movie_date=date
            ).values_list(
                "seat_number", flat=True
            )  # no flat=True means it returns list of tuples
            seats = list(query_set)

            print(seats)
            seats = " ".join(seats)
            context = {"reserved_seats": seats}
            print(data)
            return render(request, "Movies/seatView.html", context)
        except Exception as e:
            print(e)
            return HttpResponse("<h3>something went wrong</h3>")
    else:
        return HttpResponse("<h3>Invalid request</h3>")



def reserved_seats(request):
    if request.method == 'GET':
        try:
            print("reserved sets-------->")
            date = request.session["movie_date"]
            print(date)
            title = request.session["movie_title"]
            print(title)
            query_set = Ticket.objects.filter(
                movie_title=title, movie_date=date
            ).values_list(
                "seat_number", flat=True
            )  # no flat=True means it returns list of tuples
            seats = list(query_set)
            print(seats)
            seats = " ".join(seats)
            context = {"reserved_seats": seats}
            return JsonResponse(context)
        except Exception as e:
            print(e)
            return HttpResponse("internal server error")
    return HttpResponse("Method not allowed!")