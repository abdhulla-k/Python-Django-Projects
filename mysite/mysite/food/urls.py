from django.urls import path
from . import views

# app_name = 'food'     # this is the method of Name spacing
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:item_id>/', views.detail, name = 'detail'),
    # add items
    path('add/', views.create_item, name = 'create_item'),
    # edit
    path('update/<int:id>', views.update_item, name= 'update_item'),
    # delete
    path('delete/<int:id>', views.delete_item, name = 'delete_item')
]