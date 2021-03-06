# Generated by Django 3.2.5 on 2021-08-29 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the Geographical Location (e.g. Africa, Asia)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the Topic (e.g. Fashion, Tech, Sports)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('Z', 'Would rather not say'), ('UK', 'Unknown')], help_text='Select your gender', max_length=2, null=True)),
                ('bio', models.CharField(blank=True, help_text='Tell your readers about yourself...', max_length=1000, null=True, verbose_name='About the Writer')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('city', models.CharField(blank=True, help_text='Where do you live?', max_length=255, null=True, verbose_name='City')),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Enter your LinkedIn URL here', null=True, verbose_name='LinkedIn')),
                ('twitter', models.URLField(blank=True, help_text='Enter your Twitter URL here', null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, help_text='Enter your Instagram URL here', null=True, verbose_name='Instagram')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('geolocation', models.ManyToManyField(help_text='Select a geolocations for this blog', to='blog.Geolocation')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profile')),
                ('topic', models.ManyToManyField(help_text='Select topic(s) for this blog', to='blog.Topic')),
            ],
        ),
    ]
