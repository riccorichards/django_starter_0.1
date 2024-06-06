from django.urls import path
from . import views

path("notes/", views.NoteListCreate.as_view, name="notes-list"),
path("notes/delete/<int:pk>/", views.NoteDelete, name="delete-note")

