from django.urls import path, include
from . import views

urlpatterns = [
    # path('add-movie',views.addMovie, name='add-movie'),
    # path('buy/', views.Buy())
    path("ticket/date", views.ticket_date, name="get_ticket_date"),
    path("ticket", views.book_ticket, name="book_ticket"),
    path("reservedseats", views.reserved_seats, name="get_reserved_seats"),
    path("buywithpoint", views.buyWithPoint, name="buy-with-points"),
    path("seatview", views.seatView, name="seat-view"),
]


# localhost:8000/buy/
