import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here
class Profile(models.Model): #User Profile
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-binary'),
        ('Z', 'Would rather not say'),
        ('UK', 'Unknown'),)
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES,
                           help_text='Select your gender', blank=True, null=True)
    bio = models.CharField(verbose_name="About the Writer", max_length=1000,
                           help_text='Tell your readers about yourself...', blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=255,
                            help_text='Where do you live?', blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    linkedin = models.URLField(verbose_name='LinkedIn', max_length = 200,
                               help_text='Enter your LinkedIn URL here',
                               blank=True, null=True)
    twitter = models.URLField(verbose_name='Twitter', max_length = 200,
                              help_text='Enter your Twitter URL here',
                              blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram', max_length = 200,
                               help_text='Enter your Instagram URL here', blank=True, null=True)
'''
    def __str__(self):  # __unicode__ for Python 2
        return self.author.username
'''
    def is_eighteenyrs(self):
        age = datetime.date.today() - self.date_of_birth
        return age >= 18

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(author=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# - - - - - - - - -
class Topic(models.Model):
    """Model representing the topic being discussed."""
    name = models.CharField(max_length=200, help_text='Enter the Topic (e.g. Fashion, Tech, Sports)')

    def __str__(self):
        """String for representing the Geolocation object."""
        return self.name
# ------------------------
class Geolocation(models.Model):
    """Model representing Geographical location of the topic being discussed."""
    name = models.CharField(max_length=200, help_text='Enter the Geographical Location (e.g. Africa, Asia)')

    def __str__(self):
        """String for representing the Geolocation object."""
        return self.name
# ------------------------
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    #updated = models.DateTimeField(auto_now=True)
    topic = models.ManyToManyField(Topic, help_text='Select topic(s) for this blog')
    geolocation = models.ManyToManyField(Geolocation, help_text='Select a geolocations for this blog')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def display_topic(self):
        """Create a string for the Topic. This is required to display topic in Admin."""
        return ', '.join(topic.name for topic in self.topic.all()[:3])
    display_topic.short_description = 'Topic'

    def display_geolocation(self):
        """Create a string for the Geolocation."""
        return ', '.join(geolocation.name for geolocation in self.geolocation.all()[:3])
    display_geolocation.short_description = 'Geolocation'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])



