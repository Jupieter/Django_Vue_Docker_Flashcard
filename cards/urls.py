from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'cards'

urlpatterns = [
    # path("", TemplateView.as_view(template_name="cards/base.html"), name="home"),
    path("", views.CardListView.as_view(), name="card-list"),
    path("<int:pk>", views.SetListView.as_view(), name="set-list"),
    path("set_change", views.set_change, name='set_change'),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>",views.BoxView.as_view(), name="box"),
]