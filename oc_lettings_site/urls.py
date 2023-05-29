from django.contrib import admin
from django.urls import path
from lettings import views as lettings_view
from profiles import views as profiles_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings_view.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings_view.letting, name='letting'),
    path('profiles/', profiles_view.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_view.profile, name='profile'),
    path('admin/', admin.site.urls),
]
