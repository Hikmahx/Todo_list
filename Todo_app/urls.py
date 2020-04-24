from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),#calls the index fxn of view
    path('details/<int:id>/', views.details, name="details"),
    path('add_item/', views.add_item),
    path('delete_todo/<int:id>', views.delete_item),#url for deleting a specific item via its id
]