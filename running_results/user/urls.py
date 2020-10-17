from django.urls import path
from .views import (
    user_create_view, 
    user_detail_view, 
    user_delete_view,
    user_list_view,
    user_update_view,
    
)

app_name = 'user'
urlpatterns = [
    path('', user_list_view, name='user-list'),
    path('create/', user_create_view, name='user-create'),
    path('<int:id>/', user_detail_view, name='user-detail'),
    path('<int:id>/update/', user_update_view, name='user-update'),
    path('<int:id>/delete/', user_delete_view, name='user-delete'),
]