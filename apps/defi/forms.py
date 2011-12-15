# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, widgets
from django.forms.extras.widgets import SelectDateWidget
from JustDoThat.apps.defi.models import Defi
from django.db import models
from datetime import date
from django.forms.fields import IntegerField, DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, Select





class DefiForm(ModelForm):
	liste = ((1,'Easy'), (2,'Normal'),(3,'Hard'), (4,'Very Hard'))    
	difficulte = forms.ChoiceField(label='Difficulty', choices=liste, required=True)
	fin = forms.DateField(label='End',required=True)
	titre = forms.CharField(label='Title', max_length=45, required=True)
	# categorie = forms.IntegerField(label='Category', required=True)
	
	class Meta:
		model = Defi
		exclude = ('slug','debut','createur','fini',)
        
		
	def __init__(self, *args, **kwargs):
			 super(DefiForm, self).__init__(*args, **kwargs)
			 this_year = date.today().year
			 years = range(this_year, this_year+2)
			 self.fields['fin'].widget = SelectDateWidget(years=years)
			 self.fields['categorie'].label = 'Category'

			 

			 
		
        
   