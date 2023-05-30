from django.urls import path 
from .views import *

app_name = 'api'

# define the urls
urlpatterns = [
    path('all_set/', card_set, name="card-set"),
    # path('tasks/<int:pk>/', card_set),
    path('create_set/', create_card_set, name='create-card-set'),
    path('delete_set/<int:pk>', delete_card_set, name='delete-card-set'),
]