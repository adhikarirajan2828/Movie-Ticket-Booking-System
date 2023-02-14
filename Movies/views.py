from django.shortcuts import render,redirect
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