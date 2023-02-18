from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-note/', views.create_note, name='create_note'),
    path('update-note/<int:note_id>', views.update_note, name='update_note'),
    path('delete-note/<int:note_id>', views.delete_note, name='delete_note')
]
