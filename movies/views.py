from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Movie, MovieForm

# Create your views here.

class IndexView(ListView):
	template_name = 'movies/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		owned = Movie.objects.filter(status='O')
		count = len(owned)
		genre_list = {}
		for movie in owned:
			g = movie.get_genre_display()
			if(g in genre_list):
				genre_list[g] = genre_list[g] + 1
			else:
				genre_list[g] = 1

		context['count'] = count
		context['genres'] = genre_list
		return context

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
	if(request.method == 'POST'):
		form = MovieForm(request.POST)
		if(form.is_valid()):
			form.save()
			return render(request, 'movies/index.html')
	else:
		return render(request, 'movies/addmovie.html', {'form' : MovieForm()})

def edit_movie(request, pk):
	m = Movie.objects.get(pk=pk)
	if(request.method == 'POST'):
		form = MovieForm(request.POST, instance=m)
		print("got here");
		if(form.is_valid()):
			print("and here")
			form.save()
			return render(request, 'movies/index.html')
	else:
		return render(request, 'movies/editmovie.html',
			{'form' : MovieForm(instance=m)})

def delete_movie(request, pk):
	m = Movie.objects.get(pk=pk)
	if(request.method == 'POST'):
		m.delete()
		return render(request, 'movies/index.html')
		#return render(request, 'movies/index.html')
	else:
		#return HttpResponse("not deleted")
		return render(request, 'movies/deletemovie.html',
			{'movie' : m})
