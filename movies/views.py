from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Movie, MovieForm, SearchForm

# Create your views here.

class IndexView(ListView):
	template_name = 'movies/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		owned = Movie.objects.filter(status='O')
		count = len(owned)
		genre_list = [x[1] for x in Movie.GENRES]
		genre_dict = {}
		for genre in genre_list:
			genre_dict[genre] = 0

		for movie in owned:
			g = movie.get_genre_display()
			genre_dict[g] = genre_dict[g] + 1

		context['count'] = count
		context['genres'] = genre_dict
		return context

	def get_queryset(self):
		return

class MoviesWishListView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/wishlist.html'

	def get_queryset(self):
		return Movie.objects.filter(status="W").order_by('title')

class MoviesOwnedView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/owned.html'

	def get_queryset(self):
		return Movie.objects.filter(status="O").order_by('title')

class MoviesOwnedGenreView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/genredetail.html'

	def get_context_data(self, **kwargs):
		context = super(MoviesOwnedGenreView, self).get_context_data(**kwargs)
		context.update({'genre': self.kwargs['genre']})
		return context

	def get_queryset(self):
		genre = self.kwargs['genre']
		print("genre: " + genre)
		for g in Movie.GENRES:
			print(g[1])
			if(g[1] == genre):
				genre = g[0];
				print(genre)
				break;
		return Movie.objects.filter(genre=genre).order_by('title')

class MoviesDetailView(DetailView):
	model = Movie
	template_name = 'movies/detail.html'


def add_movie(request):
	if(request.method == 'POST'):
		form = MovieForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('movies:index'))
	else:
		return render(request, 'movies/addmovie.html', {'form' : MovieForm()})

def edit_movie(request, pk):
	m = Movie.objects.get(pk=pk)
	if(request.method == 'POST'):
		form = MovieForm(request.POST, instance=m)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('movies:index'))
	else:
		return render(request, 'movies/editmovie.html',
			{'form' : MovieForm(instance=m)})

def delete_movie(request, pk):
	m = Movie.objects.get(pk=pk)
	if(request.method == 'POST'):
		m.delete()
		return HttpResponseRedirect(reverse('movies:index'))
		#return render(request, 'movies/index.html')
	else:
		#return HttpResponse("not deleted")
		return render(request, 'movies/deletemovie.html', {'movie' : m})

def search_movie(request):
	title = request.GET['search_query']
	close = None
	if(title == ""):
		title = "[blank]";
	try:
		movie = Movie.objects.get(title__iexact=title)
	except Movie.DoesNotExist:
		close = Movie.objects.filter(title__icontains=title)
		if(not close):
			return render(request, 'movies/searchmovie.html', {'not_found' : title})

	if(close == None):
		return render(request, 'movies/searchmovie.html', {'found' : movie})
	else:
		return render(request, 'movies/searchmovie.html',
			{'partial' : close, 'query' : title})
