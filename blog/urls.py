from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListAllPublishedView.as_view(), name='posts-all-published'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('myarticles/', views.PostsByUserListView.as_view(), name='my-posts'),
    #path('author/<int:pk>', views.author_profile, name='author-info'),
    #path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-info'),
]

urlpatterns += [
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
]