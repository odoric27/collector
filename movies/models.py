from django.db import models
from django import forms
from django.core import validators

# Create your models here.

class Movie(models.Model):
	GENRES = (
		('act', 'Action'),
		('com', 'Comedy'),
		('dra', 'Drama'),
		('fan', 'Fantasy'),
		('hor', 'Horror'),
		('sci', 'Science Fiction'),
		('doc', 'Documentary'),
		('rom', 'Romance'),
		('unk', 'Unknown'))
	STATUS = (
		('O', 'Owned'),
		('W', 'Wishlist'))

	status = models.CharField(
		max_length=1, 
		choices=STATUS, 
		null=False, 
		default='O')
	title = models.CharField(max_length=100)
	runtime = models.PositiveIntegerField(default=0, blank=True)
	director = models.CharField(
		max_length=50,
		blank=True,
		validators=[validators.RegexValidator(
			regex=r'[A-Za-z]',
			message="Illegal characters. Use letters only")])
	genre = models.CharField(
		max_length=3,
		blank=False,
		default='unk',
		choices=GENRES)
	year = models.CharField(
		max_length=4,
		blank=True,
		validators=[validators.RegexValidator(
			regex=r'[0-9]',
			message="Illegal characters. Use numbers only")])

	def __str__(self):
		return self.title

class MovieForm(forms.ModelForm):
		class Meta:
			model = Movie
			fields = ['status', 'title', 'runtime',
					  'director', 'genre', 'year']
			unique_together = ("title", "director", "year")

class SearchForm(forms.Form):
	search_query = forms.CharField(
		max_length=100,
		help_text='Enter movie title')