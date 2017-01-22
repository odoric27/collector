from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'movies'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url('owned-cover/$', views.MoviesOwnedCoverView.as_view(), name='owned-cover'),
    url('owned-list/$', views.MoviesOwnedListView.as_view(), name='owned-list'),
    url('wishlist/$', views.MoviesWishListView.as_view(), name='wishlist'),
    url('wishlist-cover/$', views.MoviesWishListCoverView.as_view(), name='wishlist-cover'),
    url(r'^(?P<pk>[0-9]+)/$', views.MoviesDetailView.as_view(), name='detail'),
    url(r'^(?P<title>[A-Za-z ]+)/addmovie/$', views.add_from_search, name='addfromsearch'),
    url('addmovie/$', views.add_movie, name='addmovie'),
    url('searchmovie/$', views.search_movie, name='searchmovie'),
    url(r'^(?P<genre>[A-Za-z ]+)/genredetail/$', views.MoviesOwnedGenreView.as_view(), name='genredetail'),
    url(r'^(?P<pk>[0-9]+)/editmovie/$', views.edit_movie, name='editmovie'),
    url(r'^(?P<pk>[0-9]+)/deletemovie/$', views.delete_movie, name='deletemovie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
