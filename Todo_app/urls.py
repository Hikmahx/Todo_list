from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),#calls the index fxn of view
    path('details/<int:id>/', views.details, name="details"),
    path('add_item/', views.add_item),
]