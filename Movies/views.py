from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Ticket
import json


# from django.views.generic import ListView, DetailView
# from .models import Movies
# # Create your views here.

# class HomeView(ListView):
#     model = Movies
#     template_name = 'templates/index.html'
# from Movies.forms import AddMovieForm
# from django.views.generic import ListView, DetailView, CreateView

# def addMovie(request):
#     mydict={}
#     form=AddMovieForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     else:
#          print("Hello")
#     mydict['form']=form
#     return render(request,'templates/Movies/add_movie.html',mydict)

# def buyTickets(request):
#     data = request.body
#     print(data)

def ticket_date(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            print(data)
            date = data['date']
            request.session['ticket_date'] = date
            print(request.session['ticket_date'])
            response = {
                "status": 200,
                "message": "success"
            }
            return render(request,'Movies/seatView.html', response)
    except:
        response = {
            "error":"something went wrong"
        }
        return HttpResponse(response)
        

@csrf_exempt
def book_ticket(request):
    if request.method == 'POST':
        data = data = json.loads(request.body)
        Ticket.objects.create(
                movie_title = data['movieName'],
                seat_number = data['seatSelectedNumber'],
                price = data['ticketPrice'],
                # total_selected_seats = data['totalSeatCount'],
                # movie_date = request.session['ticket_date']
                )
        response = {
                "message":"ticket saved!",
                "status":200,
                "payload":{}
                }
        return HttpResponse(response)    
    return HttpResponse("Something went wrong!")


