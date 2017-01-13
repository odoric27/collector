from django.db import models
from django.forms import ModelForm
from django.core import validators

# Create your models here.
class Movie(models.Model):
	action = 'A'
	comedy = 'C'
	drama = 'Dr'
	fantasy = 'F'
	horror = 'H'
	scifi = 'S'
	doc = 'Do'
	GENRES = (
		(action, 'Action'),
		(comedy, 'Comedy'),
		(drama, 'Drama'),
		(fantasy, 'Fantasy'),
		(horror, 'Horror'),
		(scifi, 'Sci-Fi'),
		(doc, 'Documentary'))

	owned = 'O'
	wishlist = 'W'
	STATUS = (
		(owned, 'Owned'),
		(wishlist, 'Wishlist'))

	status = models.CharField(
		max_length=1, 
		choices=STATUS, 
		null=False, 
		default=owned)
	title = models.CharField(max_length=100)
	runtime = models.PositiveIntegerField(default=0, blank=True)
	director = models.CharField(
		max_length=50,
		blank=True,
		validators=[validators.RegexValidator(
			regex=r'[A-Za-z]',
			message="Illegal characters. Use letters only")])
	genre = models.CharField(
		max_length=10,
		blank=True,
		choices=GENRES)

	def __str__(self):
		return self.title
'''
class MovieForm(forms.Form):
	owned = forms.BooleanField()
	wishlist = forms.BooleanField()
	title = forms.CharField(max_length=100)
	runtime = forms.IntegerField()
	director_first_name = forms.CharField(max_length=30)
	director_last_name = forms.CharField(max_length=30)
	genre = forms.CharField(max_length=10)
'''

class MovieForm(ModelForm):
		class Meta:
			model = Movie
			fields = ['status', 'title', 'runtime',
					  'director', 'genre']