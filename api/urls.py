from django.urls import path 
from .views import card_set

app_name = 'api'

# define the urls
urlpatterns = [
    path('all_set/', card_set, name="card_set"),
    # path('tasks/<int:pk>/', card_set),
]