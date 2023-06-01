from django.urls import path
from . import views as lettings_view

app_name = 'lettings'

urlpatterns = [
    path('', lettings_view.index, name='lettings_index'),
]
