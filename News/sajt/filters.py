
from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, CharFilter, DateFilter
from .models import Post, User, Author
from django import forms

class PostFilter(FilterSet):
   avtor = ModelChoiceFilter(field_name='author__user',queryset=User.objects.all(),label='автор')
   head = CharFilter(field_name='head', lookup_expr='contains',label='заголовок')
   datetime_in = DateFilter(
      field_name='datetime_in',
      lookup_expr='gte', #lookup_expr='lt',
      label='дата добавления',
      widget=forms.DateInput(attrs={ 'type': 'date'})
   )

   #price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
   # class Meta:
   #     model = Post
   #     fields = {
   #         'head': ['contains'],
   #         #'author__user': ['exact'],
   #         #'datetime_in': ['contains'],
   #     }


# class Name_of_Filter(django_filters.FilterSet):
# # example of how to set custom labels
# your_field_name = django_filters.WhateverFilterYouWantHere(label='Whatever you want')
# class Meta:
#     model = Your_Model_Here
#     fields = ['your_field_name']
#     # could also do something like '__all__' to get all the fields for that table just have to refer to your models to get the field name
#
