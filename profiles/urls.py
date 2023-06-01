from django.urls import path
from . import views as profiles_views

app_name = 'profiles'

urlpatterns = [
    path('', profiles_views.index, name='profiles_index'),
]
