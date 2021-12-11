from django.urls import path
from django.urls import path
<<<<<<< HEAD
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView
urlpatterns=[
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name='post_edit'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
=======
from .views import BlogListView,BlogDetailView,BlogCreateView
urlpatterns=[
    path('post/new/',BlogCreateView.as_view(),name='post_new'),         #forms
>>>>>>> 61efa8e2388f5025baa874c4cafb268c0ed50665
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'), # new
    path('',BlogListView.as_view(),name='home'),
]