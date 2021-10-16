from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post, Profile

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    sex = forms.CharField(help_text='Select your gender')
    bio = forms.CharField(help_text='Tell your readers about yourself...')
    city = forms.CharField(help_text='Where do you live?')
    phone = forms.IntegerField()
    linkedin = forms.URLField(help_text='Enter your LinkedIn URL here')
    twitter = forms.URLField(help_text='Enter your Twitter URL here')
    instagram = forms.URLField(help_text='Enter your Instagram URL here')

    class Meta:
        model = User
        #fields = ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2')
        fields = ('first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2', 'sex',
            'bio',
            'date_of_birth',
            'city',
            'phone',
            'linkedin',
            'twitter',
            'instagram')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']



'''class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        #fields ='__all__'   #('url', 'location', 'company')
        fields = (
            'sex',
            'bio',
            'date_of_birth',
            'city',
            'phone',
            'linkedin',
            'twitter',
            'instagram'
        )

class EditProfileForm(UserChangeForm):
    template_name='/blog/profile_form.html'
    class Meta:
        model = User
        fields = (
            'sex',
            'bio',
            'date_of_birth',
            'city',
            'phone',
            'linkedin',
            'twitter',
            'instagram'
        )
'''