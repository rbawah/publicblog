from django.urls import path
from django.conf.urls import url
from . import views


#app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListAllPublishedView.as_view(), name='posts-all-published'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('myarticles/', views.PostsByUserListView.as_view(), name='my-posts'),

]


urlpatterns += [
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('authorinfo/<int:pk>', views.PostDetailView.as_view(), name='post-author-info'),
] + [path('signup/', views.SignUpView, name='signup'),
     url(r'^profile/edit/$', views.edit_user, name='profile-update'),
    #url(r'profile/(?P<username>[a-zA-Z0-9]+)$/', views.get_user_profile, name='user-info'),
    url(r'^profile/$', views.get_user_profile, name='user-info'),
    #url(r'^profile/(?P<pk>\d+)/$', views.get_user_profile, name='user-info-with-pk'),
     path('profile/<int:pk>', views.get_user_profile, name='user-info'),

    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.view_user_profile, name='author-info'),
    url(r'articlesbyauthor/(?P<username>[a-zA-Z0-9]+)$', views.get_articles_by_author, name='author-articles'),
     ]



'''urlpatterns += [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        blog_views.activate, name='activate'),
        
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'template_name': 'blog/reset_password.html', 'post_reset_redirect': 'blog:password_reset_done', 'email_template_name': 'blog/reset_password_email.html'}, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'blog/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'blog/reset_password_confirm.html', 'post_reset_redirect': 'blog:password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'blog/reset_password_complete.html'}, name='password_reset_complete')
     
]'''