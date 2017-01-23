from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, MovieForm, SearchForm
from django.conf import settings

import os

# Create your views here.

class IndexView(ListView):
	template_name = 'movies/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		movies = Movie.objects.all()
		count = len(movies)
		genre_list = [x[1] for x in Movie.GENRES]
		genre_dict = {}
		for genre in genre_list:
			genre_dict[genre] = 0

		for movie in movies:
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

class MoviesWishListCoverView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/wishlist-cover.html'

	def get_queryset(self):
		return Movie.objects.filter(status="W").order_by('title')

class MoviesOwnedCoverView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/owned-cover.html'

	def get_queryset(self):
		return Movie.objects.filter(status="O").order_by('title')

class MoviesOwnedListView(ListView):
	context_object_name = 'movies'
	template_name = 'movies/owned-list.html'

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
			if(g[1] == genre):
				genre = g[0];
				break;
		return Movie.objects.filter(genre=genre).order_by('title')

class MoviesDetailView(DetailView):
	model = Movie
	template_name = 'movies/detail.html'


def add_from_search(request, title):
	now = timezone.localtime(timezone.now())
	form = MovieForm({'title':title, 'status':'O',
					  'genre':'unk', 'runtime':0,
					  'date_added':now})
	if(request.method == 'POST'):
		form = MovieForm(request.POST, request.FILES)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('movies:index'))
		
	return render(request, 'movies/addmovie.html', {'form' : form})

def add_movie(request):
	form = MovieForm()
	if(request.method == 'POST'):
		form = MovieForm(request.POST, request.FILES)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('movies:index'))
		
	return render(request, 'movies/addmovie.html', {'form' : form})

def edit_movie(request, pk):
	m = Movie.objects.get(pk=pk)
	form = MovieForm(instance=m)
	if(request.method == 'POST'):
		form = MovieForm(request.POST, request.FILES)
		if(form.is_valid()):
			form.save()
			m.delete()
			return HttpResponseRedirect(reverse('movies:index'))
	
	return render(request, 'movies/editmovie.html', {'form' : form})

def delete_movie(request, pk):
	m = Movie.objects.get(pk=pk)
	if(request.method == 'POST'):
		m.delete()
		try:
			#if movie has images, delete them
			orig = m.cover.url
			med = m.cover.medium.url
			thumb = m.cover.thumbnail.url
			orig_path = settings.MEDIA_ROOT + orig[6:]
			med_path = settings.MEDIA_ROOT + med[6:]
			thumb_path = settings.MEDIA_ROOT + thumb[6:]
			os.remove(orig_path)
			os.remove(med_path)
			os.remove(thumb_path)
		except ValueError:
			pass
		return HttpResponseRedirect(reverse('movies:index'))
	else:
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
