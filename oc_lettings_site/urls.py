from django.contrib import admin
from django.urls import path, include
from lettings import views as lettings_view
from profiles import views as profiles_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('lettings/<int:letting_id>/', lettings_view.letting, name='letting'),

    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('profiles/<str:username>/', profiles_view.profile, name='profile'),

    path('admin/', admin.site.urls),
]
