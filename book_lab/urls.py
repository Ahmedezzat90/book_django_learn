from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_book,name='all_book' ),
    path('add_book',views.add_book,name='add_book' ),
    path('edit_book/<int:id>/',views.edit_book,name='edit_book' ),
    path('delete_book/<int:id>/',views.delete_book,name='delete_book' ),
    path('show_details/<int:id>/',views.show_details,name='show_details' ),
    # _________________________ rest framework ________________________
    path('api/all', views.all_book_api),
    path('api/add', views.add_book_api),
    #-------------------------------
    path('api/book/<int:id>/edit', views.edit_book_api),
    path('api/book/<int:id>/delete', views.delete_book_api),
]