from django.urls import path
from .views import (
   PostsList, PostsDetail,
   ArtikullsList, ArtikullsDetail,
   PostsListSearch, ArtikullsListSearch,
   PostCreate, PostUpdate, PostDelete,
   ArtikullCreate, ArtikullUpdate, ArtikullDelete, CategoryList, subscribe, unsubscribe
)

urlpatterns = [
   path('news/', PostsList.as_view(), name= 'posts_list'),
   path('news/search/', PostsListSearch.as_view(), name= 'posts_search'),
   path('news/<int:pk>/', PostsDetail.as_view(), name= 'posts_detail'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

   path('artikulls/', ArtikullsList.as_view(), name= 'artikulls_list'),
   path('artikulls/search/', ArtikullsListSearch.as_view(), name= 'artikulls_search'),
   path('artikulls/<int:pk>/', ArtikullsDetail.as_view(), name= 'artikulls_detail'),
   path('artikulls/create/', ArtikullCreate.as_view(), name='artikull_create'),
   path('artikulls/<int:pk>/edit/', ArtikullUpdate.as_view(), name='artikull_update'),
   path('artikulls/<int:pk>/delete/', ArtikullDelete.as_view(), name='artikull_delete'),
   path('categories/<int:pk>/', CategoryList.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),

]

