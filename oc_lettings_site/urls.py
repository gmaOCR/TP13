from django.contrib import admin
from django.urls import path, include
from lettings import views as lettings_view
from profiles import views as profiles_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),

    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),

    path('admin/', admin.site.urls),
]
