from django.urls import path
from . import views as lettings_view

app_name = 'lettings'

urlpatterns = [
    path('', lettings_view.index, name='lettings_index'),
    path('<int:letting_id>/', lettings_view.letting, name='letting'),
]
