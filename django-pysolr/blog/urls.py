from django.urls import path
from . import views

urlpatterns = [
    path('search/', 
        views.SearchView.as_view(), 
        name= 'blog_search'),
    path('search_autocomplete/', 
        views.SearchAutocompleteView.as_view(),
        name = 'search-autocomplete'),
    path('search_autocomplete/title/', 
        views.autocomplete_title, 
        name = 'autocomplete_title'),
    path('search_autocomplete/detail/',
        views.autocomplete_detail,
        name = 'autocomplete_detail')
]

