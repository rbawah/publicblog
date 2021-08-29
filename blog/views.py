from django.shortcuts import render
from .models import Post, Profile#, Topic, Geolocation
from django.utils import timezone
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """View function for home page of site."""
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')

    context = {
        'posts': posts,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PostListAllPublishedView(generic.ListView):
    model = Post
    template_name = 'blog/post_list_all_published.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('published_date')
        #return Post.objects.filter(status__exact='published').order_by('published_date') #Add later

class PostDetailView(generic.DetailView):
    model = Post


from django.contrib.auth.mixins import LoginRequiredMixin
class PostsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing posts by current user."""
    model = Post
    template_name ='blog/posts_published_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('published_date')


# ---------
# Generic editing views below:
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from blog.models import Post

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text', 'topic', 'geolocation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text', 'topic', 'geolocation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

'''
class AuthorDetailView(DetailView):
    model = User
'''

'''
def author_profile(request, pk):
    user = User.objects.get(pk=pk)
    ctx = {'user':user}
    template = 'blog/author_detail.html'
    return render(request, template, ctx)
'''

'''
#UserProile
def profile_view(request, user_id):
    user = settings.AUTH_USER_MODEL.objects.get(pk=user_id)
    name = user.get_full_name()
    #user = get_object_or_404(User, pk=pk)
    bio = user.profile.bio
    city = user.profile.city
    phone = user.profile.phone
    sex = user.profile.sex
    dob = user.profile.date_of_birth
    linkedin = user.profile.linkedin
    twitter = user.profile.twitter
    instagram = user.profile.instagram

    ctx = {
        'name':name,
        'bio':bio,
        'city': city,
        'phone': phone,
        'sex': sex,
        'dob': dob,
        'linkedin': linkedin,
        'twitter': twitter,
        'instagram': instagram,
    }

    return render(request, 'author_profile.html', ctx=ctx)
'''


