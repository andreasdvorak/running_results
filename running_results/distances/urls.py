from django.urls import path
from .views import (
    distances_list_view,
    distance_detail_view,
)

app_name = 'distances'
urlpatterns = [
    path('', distances_list_view, name='distances-list'),
    path('<int:id>/', distance_detail_view, name='distance-details'),
]