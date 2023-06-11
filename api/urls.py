from django.urls import path 
from .views import *
from django.urls import path
from .views import register, LoginView, LogoutView
from knox import views as knox_views

app_name = 'api'

# define the urls
urlpatterns = [
    path('all_set/', card_set, name="card-set"),
    # path('tasks/<int:pk>/', card_set),
    path('create_set/', create_card_set, name='create-card-set'),
    path('delete_set/<int:pk>', delete_card_set, name='delete-card-set'),
    path('set_updated/<int:pk>', update_cardset, name='cupdate_cardset'),
    path('set_checked/<int:pk>', cardset_checked_view, name='cardset-checked-view'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]