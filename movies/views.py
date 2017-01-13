from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Movie, MovieForm

# Create your views here.


class IndexView(ListView):
	template_name = 'movies/index.html'

	def get_queryset(self):
		return

class MoviesWishListView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/wishlist.html'

	def get_queryset(self):
		return Movie.objects.order_by('title')

class MoviesOwnedView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/owned.html'

	def get_queryset(self):
		return Movie.objects.order_by('title')

class MoviesDetailView(DetailView):
	model = Movie
	template_name = 'movies/detail.html'


def add_movie(request):
	form = MovieForm(request.POST)
	if(form.is_valid()):
		form.save();
		return render(request, 'movies/index.html')
	else:
		return render(request, 'movies/addmovie.html', {'form' : form})


