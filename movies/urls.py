from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'movies'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url('owned/$', views.MoviesOwnedView.as_view(), name='owned'),
    url('wishlist/$', views.MoviesWishListView.as_view(), name='wishlist'),
    url(r'^(?P<pk>[0-9]+)/$', views.MoviesDetailView.as_view(), name='detail'),
    url('addmovie/$', views.add_movie, name='addmovie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
