from django.urls import path
from note_app import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('note', views.note_view, name = 'note-view' ),
    path('edit/<int:id>', views.edit, name = 'edit' ),
    path('delete/<int:id>', views.delete, name = 'delete' ),
    path('view/<int:id>', views.view, name = 'view' ),
]