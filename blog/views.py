from django.shortcuts import render
from .models import Post, Profile#, Topic, Geolocation
from django.utils import timezone
from django.views import generic
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import PasswordChangeForm

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

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from blog.forms import SignUpForm
from blog.tokens import account_activation_token

'''
@login_required
def home(request):
    return render(request, 'home.html')
'''
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required() #User's view of own profile
def get_user_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    ctx = {'user': user}
    template = 'blog/user_profile.html'
    return render(request, template, ctx)

@login_required() #View of other users/authors profile
def view_user_profile(request, username):
    author = User.objects.get(username=username)
    return render(request, 'blog/author_profile.html', {"author":author})


@login_required()
def edit_user(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    #user = User.objects.get(pk=pk)
    user_form = UserForm(instance=user)
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('user', 'sex',
            'bio',
            'date_of_birth',
            'city',
            'phone',
            'linkedin',
            'twitter',
            'instagram'))
    formset = ProfileInlineFormset(instance=user)
    if request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/blog/profile/')
        return render(request, "blog/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

def get_articles_by_author(request, username):
    posts = Post.objects.filter(author__username=username).order_by('published_date')
    author = User.objects.get(username=username)
    return render(request, 'blog/author_articles.html', {"posts": posts, "author":author})



'''@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('blog:get_user_profile'))
        else:
            return redirect(reverse('blog:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'blog/change_password.html', args)'''