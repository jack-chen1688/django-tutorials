from django.urls import path
from . import views

urlpatterns = [
    path('', 
        views.BlogListView.as_view(), 
        name='blog_list'),
    path('mine/', 
        views.MyBlogListView.as_view(), 
        name='blog_list_mine'),
    path('following/<username>/', 
        views.FollowingBlogListView.as_view(), 
        name='blog_list_following'),
    path('create/', 
        views.BlogCreateView.as_view(),
        name = 'blog_create'),
    path('<int:pk>/',
        views.BlogDetailView.as_view(),
        name='blog_detail'),
    path('<int:pk>/update/',
        views.BlogUpdateView.as_view(),
        name='blog_update'),
    path('<int:pk>/delete/', 
        views.BlogDeleteView.as_view(),
        name='blog_delete'),
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

